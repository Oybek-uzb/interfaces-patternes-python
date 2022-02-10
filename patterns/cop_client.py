from patterns.chain_of_responsibility import AbstractLoadHandler


class HardwareLoadHandler(AbstractLoadHandler):
    def handle(self, req: dict) -> bool:
        stat = req.get("stat")
        if stat is None:
            stat = {}
        cpu = req.get("cpu")
        stat["cpu"] = cpu != ""
        req["stat"] = stat
        if cpu != "":
            return super().handle(request=req)
        else:
            return False


class BIOSLoadHandler(AbstractLoadHandler):
    def handle(self, req: dict) -> bool:
        stat = req.get("stat")
        if stat is None:
            stat = {}
        bios = req.get("bios")
        stat["bios"] = bios != ""
        req["stat"] = stat
        if bios != "":
            return super().handle(request=req)
        else:
            return False


class RAMLoadHandler(AbstractLoadHandler):
    def handle(self, req: dict) -> bool:
        print("RAM")
        stat = req.get("stat")
        if stat is None:
            stat = {}
        ram = req.get("ram")
        stat["ram"] = ram != ""
        req["stat"] = stat
        if ram != "":
            return super().handle(request=req)
        else:
            return False


if __name__ == '__main__':
    hw_handler = HardwareLoadHandler()
    bios_handler = BIOSLoadHandler()
    ram_handler = RAMLoadHandler()

    hw_handler.set_next(bios_handler)
    bios_handler.set_next(ram_handler)

    request = {
        "cpu": "ASDAA",
        "bios": "",
        "ram": "True"
    }

    print(hw_handler.handle(req=request))
    print(request)
