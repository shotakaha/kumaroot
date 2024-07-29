# TOMLしたい（``TOML++``）

```cpp
#include <toml++/toml.hpp>

int main(int argc, char** argv)
{
    toml::table tbl;
    try {
        tbl = toml::parse_file(argv[1]);
        std::cout << tbl << "\n";
    }
    catch (const toml::parse_error &err)
    {
        std::cerr << "Parsing failed:\n" << err << "\n";
        return 1;
    };

    return 0;
};
```

## リファレンス

- [TOML++](https://marzer.github.io/tomlplusplus/index.html)
