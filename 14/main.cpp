#include <stdio.h>
#include <LibCore/File.h>
#include <AK/String.h>
#include <AK/HashMap.h>

i64 and_mask = 0;
i64 or_mask = 0;
i64 float_mask = 0;

HashMap<u64, u64> memory;

struct Assignment {
    u64 addr;
    u64 floating;
    u64 val;
};

void set(u64 floating, u64 addr, u64 val, size_t index=0);
void set_mask(StringView line);
u64 count_bits(u64 val);

int main(int, char**)
{
    Vector<Assignment> vals;
    auto file = Core::File::open("input", Core::IODevice::OpenMode::ReadOnly).value();
    while (!file->eof()) {
        auto line = file->read_line();
        auto parts = line.split_view(' ');
        if (parts.size() < 2) continue;
        if (parts[0] == "mask") {
            set_mask(parts[2]);
        } else {
            auto addr = parts[0].substring_view(4, parts[0].length()-5).to_int().value();
            auto val = parts[2].to_string().to_int<i64>().value();
            vals.append({(u64)(addr | or_mask), (u64)float_mask, (u64)val});
            val = (val & and_mask) | or_mask;
            memory.set(addr, val);
        }
    }
    u64 sum = 0;
    for (auto [k, v]: memory) sum += v;
    printf("Part 1: %lld\n", sum);
    memory.clear();
    // This is slow and brute forcey, only runs quickly because X's are
    // sparse :-(
    // There's probably a better solution that treats it as an inclusion-exclusion
    // problem and doesn't actually perform all the assignments
    for (auto assign: vals) {
        set(assign.floating, assign.addr, assign.val);
    }
    u64 sum2 = 0;
    for (auto [k, v]: memory) sum2 += v;
    printf("Part 2: %lld\n", sum2);
    return 0;
}

void set(u64 floating, u64 addr, u64 val, size_t index) {
    for (; index < 36; ++index) {
        const u64 bit = ((u64)1) << index;
        if (floating & bit) {
            set(floating, addr & ~bit, val, index+1);
            set(floating, addr | bit, val, index+1);
            return;
        }
    }
    memory.set(addr, val);
}

void set_mask(StringView line) {
    and_mask = or_mask = float_mask = 0;
    for (auto v: line) {
        and_mask <<= 1;
        or_mask <<= 1;
        float_mask <<= 1;
        or_mask |= (v == '1');
        and_mask |= (v != '0');
        float_mask |= v == 'X';
    }
}

u64 count_bits(u64 val) {
    u64 ans = 0;
    for (; val; val >>= 1) ans += val & 1;
    return ans;
}