#include <AK/Span.h>
#include <AK/StringUtils.h>
#include <AK/Vector.h>
#include <LibCore/File.h>
#include <stdio.h>

int window = 25;
AK::Vector<i64> values;

i64 find_invalid();
AK::Span<i64> find_range(i64 value);

int main(int, char**)
{
    auto file = Core::File::construct();
    file->set_filename("input");
    file->open(Core::IODevice::OpenMode::ReadOnly);
    for (int i = 0; !file->eof(); ++i) {
        auto line_buf = file->read_line(128);
        auto line = AK::String((const char*)line_buf.data(), line_buf.size()-1);
        if (line.length() > 0) {
            values.append(atoll(&line[0]));
        }
    }
    i64 invalid_num = find_invalid();
    printf("Part 1: %ld\n", invalid_num);
    auto range = find_range(invalid_num);
    i64 largest = 0;
    i64 smallest = INT64_MAX;
    for (auto v: range) {
        largest = max(largest, v);
        smallest = min(smallest, v);
    }
    printf("Part 2: %lld + %lld = %lld\n", smallest, largest, smallest + largest);
    return 0;
}

i64 find_invalid() {
    for (int pos = window; pos < values.size(); ++pos) {
        bool found = false;
        for (int j = pos - window; j < pos - 1; ++j) {
            for (int k = j + 1; k < pos; ++k) {
                if (values[j] + values[k] == values[pos]) {
                    found = true;
                }
            }
        }
        if (!found) {
            return values[pos];
        }
    }
    return 555;
}

AK::Span<i64> find_range(i64 value) {
    i64 i = 0;
    i64 j = 0;
    i64 sum = 0;
    while (j < values.size()) {
        if (sum < value) {
            sum += values[j++];
        } else if (sum > value) {
            sum -= values[i++];
        }
        if (sum == value) {
            return { &values[i], j - i };
        }
    }
    exit(1);
}