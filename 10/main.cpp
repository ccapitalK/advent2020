#include <AK/QuickSort.h>
#include <AK/String.h>
#include <AK/Vector.h>
#include <LibCore/File.h>
#include <stdlib.h>

int main(int, char**)
{
    AK::Vector<int> values;
    auto file = Core::File::construct();
    file->set_filename("input");
    file->open(Core::IODevice::OpenMode::ReadOnly);
    while (!file->eof()) {
        auto line_buf = file->read_line(128);
        auto line = AK::String((const char*)line_buf.data(), line_buf.size()-1);
        if (!line.is_empty()) {
            int v = line.to_int().value();
            values.append(v);
        }
    }
    values.append(0);
    quick_sort(values);
    values.append(values[values.size()-1] + 3);
    int diffs[4] = {0, 0, 0, 0};
    for (int i = 0; i < values.size() - 1; ++i) {
        int d = values[i+1] - values[i];
        ++diffs[d];
    }
    printf("Part 1: %d\n", diffs[1] * diffs[3]);
    AK::Vector<i64> dp;
    dp.resize(values.size());
    dp[0] = 1;
    for (int i = 1; i < dp.size(); ++i) {
        dp[i] = 0;
        for (int j = i - 1; j >= 0 && values[i] - values[j] <= 3; --j) {
            dp[i] += dp[j];
        }
    }
    printf("Part 2: %lld\n", dp.last());
    return 0;
}
