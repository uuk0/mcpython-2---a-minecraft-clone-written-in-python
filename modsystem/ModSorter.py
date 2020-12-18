import log


class ModSorter:
    def __init__(self, modlist):
        self.modlist = modlist
        self.modlistsorted = []
        self.modlistnames = []
        self.externaldep = {}

    def sort(self):
        for mod in self.modlist.values():
            for m in mod.register_before():
                if m not in self.externaldep:
                    self.externaldep[m] = []
                self.externaldep[m].append(mod.getName())
            for m in mod.register_after_if_present():
                if m in self.modlist.keys():
                    if mod.getName() not in self.externaldep:
                        self.externaldep[mod.getName()] = []
                    self.externaldep[mod.getName()].append(m)
        data = []
        for mod in self.modlist.values():
            depend = []
            for e in mod.getDependencies():
                depend.append(e[0])
            if mod.getName() in self.externaldep:
                depend += self.externaldep[mod.getName()]
            data.append((mod.getName(), set(depend)))
        sorteddata = self.topological_sort(data)
        for e in sorteddata:
            self.modlistsorted.append(self.modlist[e])

    def topological_sort(self, source):
        # code from https://stackoverflow.com/questions/11557241/python-sorting-a-dependency-list
        """perform topo sort on elements.

        :arg source: list of ``(name, set(names of dependancies))`` pairs
        :returns: list of names, with dependancies listed first
        """
        pending = [(name, set(deps)) for name, deps in source]
        emitted = []
        while pending:
            next_pending = []
            next_emitted = []
            for entry in pending:
                name, deps = entry
                deps.difference_update(
                    set((name,)), emitted
                )  # <-- pop self from dep, req Py2.6
                if deps:
                    next_pending.append(entry)
                else:
                    yield name
                    emitted.append(
                        name
                    )  # <-- not required, but preserves original order
                    next_emitted.append(name)
            if not next_emitted:
                raise ValueError(
                    "cyclic dependancy detected: %s %r" % (name, (next_pending,))
                )
            pending = next_pending
            emitted = next_emitted
