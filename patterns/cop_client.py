from patterns.chain_of_responsibility import AbstractLoadHandler


class HardwareLoadHandler(AbstractLoadHandler):
    def handle(self, request: dict) -> bool:
        stat = request.get("stat")
        if stat is None:
            stat = {}
        cpu = request.get("cpu")
        stat["cpu"] = cpu != ""
        request["stat"] = stat
        if cpu != "":
            return super().handle(request=request)
        else:
            return False


class BIOSLoadHandler(AbstractLoadHandler):
    def handle(self, request: dict) -> bool:
        stat = request.get("stat")
        if stat is None:
            stat = {}
        bios = request.get("bios")
        stat["bios"] = bios != ""
        request["stat"] = stat
        if bios != "":
            return super().handle(request=request)
        else:
            return False


if __name__ == '__main__':
    hw_handler = HardwareLoadHandler()
    bios_handler = BIOSLoadHandler()

    hw_handler.set_next(bios_handler)

    request = {
        "cpu": "AMD",
        "bios": "American Award BIOS"
    }

    print(hw_handler.handle(request=request))
    print(request)
