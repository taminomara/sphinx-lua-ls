"""
Linking to standard lua library.

"""

import docutils.nodes
import sphinx.addnodes
import sphinx.application
import sphinx.environment

targets = {
    "_G": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-_G"),
    "_VERSION": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-_VERSION"),
    "assert": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-assert"),
    "bit32.arshift": (["5.2"], "pdf-bit32.arshift"),
    "bit32.band": (["5.2"], "pdf-bit32.band"),
    "bit32.bnot": (["5.2"], "pdf-bit32.bnot"),
    "bit32.bor": (["5.2"], "pdf-bit32.bor"),
    "bit32.btest": (["5.2"], "pdf-bit32.btest"),
    "bit32.bxor": (["5.2"], "pdf-bit32.bxor"),
    "bit32.extract": (["5.2"], "pdf-bit32.extract"),
    "bit32.lrotate": (["5.2"], "pdf-bit32.lrotate"),
    "bit32.lshift": (["5.2"], "pdf-bit32.lshift"),
    "bit32.replace": (["5.2"], "pdf-bit32.replace"),
    "bit32.rrotate": (["5.2"], "pdf-bit32.rrotate"),
    "bit32.rshift": (["5.2"], "pdf-bit32.rshift"),
    "bit32": (["5.2"], "6.7"),
    "collectgarbage": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-collectgarbage"),
    "coroutine.close": (["5.4"], "pdf-coroutine.close"),
    "coroutine.create": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-coroutine.create"),
    "coroutine.isyieldable": (["jit", "5.3", "5.4"], "pdf-coroutine.isyieldable"),
    "coroutine.resume": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-coroutine.resume"),
    "coroutine.running": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-coroutine.running"),
    "coroutine.status": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-coroutine.status"),
    "coroutine.wrap": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-coroutine.wrap"),
    "coroutine.yield": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-coroutine.yield"),
    "coroutine": (["jit", "5.1", "5.2", "5.3", "5.4"], "6.2"),
    "debug.debug": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-debug.debug"),
    "debug.getfenv": (["5.1"], "pdf-debug.getfenv"),
    "debug.gethook": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-debug.gethook"),
    "debug.getinfo": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-debug.getinfo"),
    "debug.getlocal": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-debug.getlocal"),
    "debug.getmetatable": (
        ["jit", "5.1", "5.2", "5.3", "5.4"],
        "pdf-debug.getmetatable",
    ),
    "debug.getregistry": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-debug.getregistry"),
    "debug.getupvalue": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-debug.getupvalue"),
    "debug.getuservalue": (["jit", "5.2", "5.3", "5.4"], "pdf-debug.getuservalue"),
    "debug.setfenv": (["5.1"], "pdf-debug.setfenv"),
    "debug.sethook": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-debug.sethook"),
    "debug.setlocal": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-debug.setlocal"),
    "debug.setmetatable": (
        ["jit", "5.1", "5.2", "5.3", "5.4"],
        "pdf-debug.setmetatable",
    ),
    "debug.setupvalue": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-debug.setupvalue"),
    "debug.setuservalue": (["jit", "5.2", "5.3", "5.4"], "pdf-debug.setuservalue"),
    "debug.traceback": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-debug.traceback"),
    "debug.upvalueid": (["jit", "5.2", "5.3", "5.4"], "pdf-debug.upvalueid"),
    "debug.upvaluejoin": (["jit", "5.2", "5.3", "5.4"], "pdf-debug.upvaluejoin"),
    "debug": (["jit", "5.1", "5.2", "5.3", "5.4"], "6.10"),
    "dofile": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-dofile"),
    "error": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-error"),
    "file.close": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-file:close"),
    "file.flush": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-file:flush"),
    "file.lines": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-file:lines"),
    "file.read": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-file:read"),
    "file.seek": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-file:seek"),
    "file.setvbuf": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-file:setvbuf"),
    "file.write": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-file:write"),
    "getfenv": (["5.1"], "pdf-getfenv"),
    "getmetatable": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-getmetatable"),
    "io.close": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-io.close"),
    "io.flush": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-io.flush"),
    "io.input": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-io.input"),
    "io.lines": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-io.lines"),
    "io.open": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-io.open"),
    "io.output": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-io.output"),
    "io.popen": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-io.popen"),
    "io.read": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-io.read"),
    "io.stderr": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-io.stderr"),
    "io.stdin": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-io.stdin"),
    "io.stdout": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-io.stdout"),
    "io.tmpfile": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-io.tmpfile"),
    "io.type": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-io.type"),
    "io.write": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-io.write"),
    "io": (["jit", "5.1", "5.2", "5.3", "5.4"], "6.8"),
    "ipairs": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-ipairs"),
    "load": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-load"),
    "loadfile": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-loadfile"),
    "loadstring": (["5.1"], "pdf-loadstring"),
    "math.abs": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.abs"),
    "math.acos": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.acos"),
    "math.asin": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.asin"),
    "math.atan": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.atan"),
    "math.atan2": (["jit", "5.1", "5.2"], "pdf-math.atan2"),
    "math.ceil": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.ceil"),
    "math.cos": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.cos"),
    "math.cosh": (["jit", "5.1", "5.2"], "pdf-math.cosh"),
    "math.deg": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.deg"),
    "math.exp": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.exp"),
    "math.floor": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.floor"),
    "math.fmod": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.fmod"),
    "math.frexp": (["jit", "5.1", "5.2"], "pdf-math.frexp"),
    "math.huge": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.huge"),
    "math.ldexp": (["jit", "5.1", "5.2"], "pdf-math.ldexp"),
    "math.log": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.log"),
    "math.log10": (["5.1"], "pdf-math.log10"),
    "math.max": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.max"),
    "math.maxinteger": (["5.3", "5.4"], "pdf-math.maxinteger"),
    "math.min": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.min"),
    "math.mininteger": (["5.3", "5.4"], "pdf-math.mininteger"),
    "math.modf": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.modf"),
    "math.pi": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.pi"),
    "math.pow": (["jit", "5.1", "5.2"], "pdf-math.pow"),
    "math.rad": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.rad"),
    "math.random": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.random"),
    "math.randomseed": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.randomseed"),
    "math.sin": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.sin"),
    "math.sinh": (["jit", "5.1", "5.2"], "pdf-math.sinh"),
    "math.sqrt": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.sqrt"),
    "math.tan": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-math.tan"),
    "math.tanh": (["jit", "5.1", "5.2"], "pdf-math.tanh"),
    "math.tointeger": (["5.3", "5.4"], "pdf-math.tointeger"),
    "math.type": (["5.3", "5.4"], "pdf-math.type"),
    "math.ult": (["5.3", "5.4"], "pdf-math.ult"),
    "math": (["jit", "5.1", "5.2", "5.3", "5.4"], "6.7"),
    "metamethods": (["5.3", "5.4"], "pdf-metamethods"),
    "module": (["5.1"], "pdf-module"),
    "next": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-next"),
    "os.clock": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-os.clock"),
    "os.date": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-os.date"),
    "os.difftime": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-os.difftime"),
    "os.execute": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-os.execute"),
    "os.exit": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-os.exit"),
    "os.getenv": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-os.getenv"),
    "os.remove": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-os.remove"),
    "os.rename": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-os.rename"),
    "os.setlocale": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-os.setlocale"),
    "os.time": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-os.time"),
    "os.tmpname": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-os.tmpname"),
    "os": (["jit", "5.1", "5.2", "5.3", "5.4"], "6.9"),
    "package.config": (["5.2", "5.3", "5.4"], "pdf-package.config"),
    "package.cpath": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-package.cpath"),
    "package.loaded": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-package.loaded"),
    "package.loaders": (["5.1"], "pdf-package.loaders"),
    "package.loadlib": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-package.loadlib"),
    "package.path": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-package.path"),
    "package.preload": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-package.preload"),
    "package.searchers": (["jit", "5.2", "5.3", "5.4"], "pdf-package.searchers"),
    "package.searchpath": (["jit", "5.2", "5.3", "5.4"], "pdf-package.searchpath"),
    "package.seeall": (["5.1"], "pdf-package.seeall"),
    "package": (["jit", "5.1", "5.2", "5.3", "5.4"], "6.3"),
    "pairs": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-pairs"),
    "pcall": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-pcall"),
    "print": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-print"),
    "rawequal": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-rawequal"),
    "rawget": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-rawget"),
    "rawlen": (["5.2", "5.3", "5.4"], "pdf-rawlen"),
    "rawset": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-rawset"),
    "require": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-require"),
    "select": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-select"),
    "setfenv": (["5.1"], "pdf-setfenv"),
    "setmetatable": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-setmetatable"),
    "std.metatable.__add": (["5.3", "5.4"], "pdf-__add"),
    "std.metatable.__band": (["5.3", "5.4"], "pdf-__band"),
    "std.metatable.__bnot": (["5.3", "5.4"], "pdf-__bnot"),
    "std.metatable.__bor": (["5.3", "5.4"], "pdf-__bor"),
    "std.metatable.__bxor": (["5.3", "5.4"], "pdf-__bxor"),
    "std.metatable.__call": (["5.3", "5.4"], "pdf-__call"),
    "std.metatable.__close": (["5.4"], "pdf-__close"),
    "std.metatable.__concat": (["5.3", "5.4"], "pdf-__concat"),
    "std.metatable.__div": (["5.3", "5.4"], "pdf-__div"),
    "std.metatable.__eq": (["5.3", "5.4"], "pdf-__eq"),
    "std.metatable.__gc": (["5.3", "5.4"], "pdf-__gc"),
    "std.metatable.__idiv": (["5.3", "5.4"], "pdf-__idiv"),
    "std.metatable.__index": (["5.3", "5.4"], "pdf-__index"),
    "std.metatable.__le": (["5.3", "5.4"], "pdf-__le"),
    "std.metatable.__len": (["5.3", "5.4"], "pdf-__len"),
    "std.metatable.__lt": (["5.3", "5.4"], "pdf-__lt"),
    "std.metatable.__metatable": (["5.3", "5.4"], "pdf-__metatable"),
    "std.metatable.__mod": (["5.3", "5.4"], "pdf-__mod"),
    "std.metatable.__mode": (["5.3", "5.4"], "pdf-__mode"),
    "std.metatable.__mul": (["5.3", "5.4"], "pdf-__mul"),
    "std.metatable.__name": (["5.3", "5.4"], "pdf-__name"),
    "std.metatable.__newindex": (["5.3", "5.4"], "pdf-__newindex"),
    "std.metatable.__pairs": (["5.3", "5.4"], "pdf-__pairs"),
    "std.metatable.__pow": (["5.3", "5.4"], "pdf-__pow"),
    "std.metatable.__shl": (["5.3", "5.4"], "pdf-__shl"),
    "std.metatable.__shr": (["5.3", "5.4"], "pdf-__shr"),
    "std.metatable.__sub": (["5.3", "5.4"], "pdf-__sub"),
    "std.metatable.__tostring": (["5.3", "5.4"], "pdf-__tostring"),
    "std.metatable.__unm": (["5.3", "5.4"], "pdf-__unm"),
    "std.metatable": (["5.2", "5.3", "5.4"], "2.4"),
    "std.type": (["5.2", "5.3", "5.4"], "pdf-type"),
    "string.byte": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-string.byte"),
    "string.char": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-string.char"),
    "string.dump": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-string.dump"),
    "string.find": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-string.find"),
    "string.format": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-string.format"),
    "string.gmatch": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-string.gmatch"),
    "string.gsub": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-string.gsub"),
    "string.len": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-string.len"),
    "string.lower": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-string.lower"),
    "string.match": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-string.match"),
    "string.pack": (["5.3", "5.4"], "pdf-string.pack"),
    "string.packsize": (["5.3", "5.4"], "pdf-string.packsize"),
    "string.rep": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-string.rep"),
    "string.reverse": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-string.reverse"),
    "string.sub": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-string.sub"),
    "string.unpack": (["5.3", "5.4"], "pdf-string.unpack"),
    "string.upper": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-string.upper"),
    "table.concat": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-table.concat"),
    "table.insert": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-table.insert"),
    "table.maxn": (["5.1"], "pdf-table.maxn"),
    "table.move": (["jit", "5.3", "5.4"], "pdf-table.move"),
    "table.pack": (["jit", "5.2", "5.3", "5.4"], "pdf-table.pack"),
    "table.remove": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-table.remove"),
    "table.sort": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-table.sort"),
    "table.unpack": (["jit", "5.2", "5.3", "5.4"], "pdf-table.unpack"),
    "tonumber": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-tonumber"),
    "tostring": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-tostring"),
    "type": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-type"),
    "unpack": (["5.1"], "pdf-unpack"),
    "utf8.char": (["5.3", "5.4"], "pdf-utf8.char"),
    "utf8.charpattern": (["5.3", "5.4"], "pdf-utf8.charpattern"),
    "utf8.codepoint": (["5.3", "5.4"], "pdf-utf8.codepoint"),
    "utf8.codes": (["5.3", "5.4"], "pdf-utf8.codes"),
    "utf8.len": (["5.3", "5.4"], "pdf-utf8.len"),
    "utf8.offset": (["5.3", "5.4"], "pdf-utf8.offset"),
    "utf8": (["5.3", "5.4"], "6.5"),
    "warn": (["5.4"], "pdf-warn"),
    "xpcall": (["jit", "5.1", "5.2", "5.3", "5.4"], "pdf-xpcall"),
}

_aliases = [
    ("metatable", "std.metatable"),
    ("", "std.metatable"),
]
for name, v in targets.copy().items():
    for to, src in _aliases:
        if name.startswith(src):
            rename = name[len(src) :].lstrip(".")
            if to and rename:
                rename = f"{to}.{rename}"
            if rename:
                targets[rename] = v
del _aliases


def resolve_std_reference(
    app: sphinx.application.Sphinx,
    env: sphinx.environment.BuildEnvironment,
    node: sphinx.addnodes.pending_xref,
    contnode: docutils.nodes.Node,
):
    if node["refdomain"] == "lua" or node["reftype"] == "any":
        if target := targets.get(node["reftarget"], None):
            versions, anchor = target
            version = env.domaindata["lua"]["config"]["lua_version"] or "5.4"
            if version in versions:
                if version == "jit":
                    version = min(versions)
                uri = f"https://www.lua.org/manual/{version}/manual.html#{anchor}"
                ref = docutils.nodes.reference("", "", contnode)
                ref["refuri"] = uri
                return ref
