from setuptools import setup, Extension
import sys, os
import subprocess
from setuptools.command.build_ext import build_ext

cwd = os.path.dirname(__file__)

def add_source(name: str):
    return [
        os.path.join(cwd, "pmma", "core", "pyx_src", f"{name}.pyx"),
        os.path.join(cwd, "pmma", "core", "cpp_src", f"{name}.cpp")
        ]

if sys.platform.startswith("win"):
    compile_args = ["/O2", "/fp:fast", "/GL", "/GF", "/GS-", "/std:c++17"]
    link_args = ["/LTCG"]

    glfw_include = "H:/Downloads/CPMMA/extern/glfw-3.4.bin.WIN64/include"
    glfw_lib = "H:/Downloads/CPMMA/extern/glfw-3.4.bin.WIN64/lib-vc2022"
    glfw_libraries = [
        "glfw3",
        "user32",
        "gdi32",
        "shell32",
        "advapi32",
        "ole32",
        "oleaut32",
        "uuid",
        "comdlg32",
        "winmm",
    ]

elif sys.platform.startswith("linux"):
    compile_args = [
        "-O3", "-ffast-math", "-funroll-loops", "-fstrict-aliasing", "-fomit-frame-pointer", "-std=c++17"
    ]
    link_args = []

    glfw_include = "/usr/include"
    glfw_lib = "/usr/lib/x86_64-linux-gnu"
    glfw_libraries = ["glfw", "GL", "X11", "pthread", "Xrandr", "Xi", "dl", "m"]

elif sys.platform == "darwin":
    compile_args = [
        "-O3", "-ffast-math", "-funroll-loops", "-fstrict-aliasing", "-fomit-frame-pointer", "-std=c++17"
    ]
    link_args = []

    glfw_include = "/opt/homebrew/include"  # or /usr/local/include depending on installation
    glfw_lib = ""
    glfw_libraries = ["glfw", "Cocoa", "OpenGL", "IOKit", "CoreVideo"]
else:
    raise NotImplementedError("Unsupported platform")

class BuildSharedLib(build_ext):
    def run(self):
        # Build shared library manually here
        self.build_shared_lib()

    def build_shared_lib(self):
        sources = [os.path.join(cwd, "pmma/core/cpp_src/Components.cpp")]
        include_dirs = [os.path.join(cwd, "pmma/core/hpp_src"), glfw_include]

        if sys.platform == "win32":
            # Build with MSVC cl.exe and link.exe manually (simplified example)
            # You may want to customize this for your setup, or use CMake instead.
            cl = os.environ.get("CL", "cl")
            link = os.environ.get("LINK", "link")

            # Compile object
            obj_files = []
            for src in sources:
                obj = src.replace(".cpp", ".obj")
                cmd_compile = [cl, "/c", "/O2", "/std:c++17"]
                for inc in include_dirs:
                    cmd_compile += [f'/I{inc}']
                cmd_compile += [src, "/Fo" + obj]
                print("Compiling: " + " ".join(cmd_compile))
                subprocess.check_call(cmd_compile)
                obj_files.append(obj)

            # Link DLL
            dll_name = os.path.join(self.build_lib, "components_shared.dll")
            cmd_link = [link, "/DLL"] + obj_files + ["/OUT:" + dll_name]
            print("Linking: " + " ".join(cmd_link))
            subprocess.check_call(cmd_link)

        else:
            # Unix-like: gcc or clang
            cc = os.environ.get("CXX", "g++")

            include_flags = [f"-I{inc}" for inc in include_dirs]
            output_lib = os.path.join(self.build_lib, "libcomponents_shared.so" if sys.platform != "darwin" else "libcomponents_shared.dylib")
            cmd = [cc, "-shared", "-fPIC"] + compile_args + include_flags + sources + ["-o", output_lib] + link_args
            print("Building shared library: " + " ".join(cmd))
            subprocess.check_call(cmd)

        print("Shared library built successfully.")

components_ext = Extension(
    name="PMMA_core",
    sources=[
        "pmma/core/cpp_src/Components.cpp",
        # add other source files if needed
    ],
    language="c++",
    include_dirs=[os.path.join(cwd, "pmma", "core", "hpp_src"), glfw_include],
    library_dirs=[os.path.join(cwd, "build", "lib"), glfw_lib],
    libraries=[*glfw_libraries],
    extra_compile_args=compile_args,
    extra_link_args=link_args,
    # Important: tell setuptools to produce a shared lib (.dll/.so)
)

setup(
    name="PMMA_core",
    ext_modules=[components_ext],
    cmdclass={
        "build_ext": BuildSharedLib,  # Overrides build_ext to build shared lib first
    },
)

print("PMMA core components built successfully!")