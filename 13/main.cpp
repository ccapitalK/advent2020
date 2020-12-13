#include <LibCore/File.h>
#include <AK/HashMap.h>
#include <AK/String.h>
#include <AK/Vector.h>
#include <AK/QuickSort.h>
#include <stdio.h>

int main(int, char**)
{
    auto file = Core::File::open("input", Core::IODevice::OpenMode::ReadOnly).value();
    auto start = file->read_line().to_int<i64>().value();
    auto data = file->read_line();
    auto parts = data.split(',');
    HashMap<u64, u64> offsets;
    Vector<u64> factors;
    i64 ans = -1;
    i64 best = start;
    for (i64 i = 0; i < parts.size(); ++i) {
        const auto &s = parts[i];
        if (s == "x") continue;
        auto v = s.to_int<i64>().value();
        factors.append(v);
        offsets.set(v, i);
        if (start % v == 0) {
            ans = 0;
            best = 0;
            continue;
        }
        auto wait = v - (start % v);
        if (wait < best) {
            best = wait;
            ans = wait * v;
        }
    }
    printf("Part 1: %lld\n", ans);
    // This code assumes all bus ids are prime, they are prime in my
    // input and I would bet real money that every input generated
    // by AOC uses prime bus ids
    quick_sort(factors.begin(), factors.end());
    i64 ans2 = 0;
    for (i64 inc = 1, ind = 0; ind < factors.size();) {
        auto x = factors[ind];
        if ((ans2 + offsets.get(x).value()) % x == 0) {
            inc *= x;
            ++ind;
        } else {
            ans2 += inc;
        }
    }
    printf("Part 2: %lld\n", ans2);
    return 0;
}
