#include <AK/Assertions.h>
#include <AK/String.h>
#include <AK/Vector.h>
#include <LibCore/File.h>

using Grid = Vector<Vector<i8>>;
Grid lines;

Grid calc_next();
bool chair(int x, int y);
bool occupied(int x, int y);

int main(int, char**)
{
    auto res = Core::File::open("input", Core::IODevice::OpenMode::ReadOnly);
    if(res.is_error()) {
        perror("Open");
        return 1;
    }
    auto file = res.value();
    while (!file->eof()) {
        auto x = file->read_line(128);
        printf("%d\n", x.size());
        auto line = AK::String(ReadonlyBytes(x.bytes()));
        line = line.trim_whitespace();
        Vector<i8> bytes;
        if (line.length() > 0) {
            for (auto v: line) {
                bytes.append((i8)v);
            }
            lines.append(AK::move(bytes));
            dbg() << line;
        }
    }
    return 0;
    i64 h = lines.size();
    i64 w = lines[0].size();
    for (int i = 0; ; ++i) {
        auto next = calc_next();
        bool diff = false;
        printf("Round %d\n", i);
        for (int y = 0; y < h; ++y) {
            for (int x = 0; x < w; ++x) {
                if (lines[y][x] != next[y][x]) diff = true;
            }
        }
        if (!diff) break;
        lines = next;
    }
    int count = 0;
    for (int y = 0; y < h; ++y) {
        for (int x = 0; x < w; ++x) {
            count += lines[y][x] == '#';
        }
    }
    printf("%d\n", count);
    return 0;
}

bool chair(int x, int y) {
    return lines[y][x] != '.';
}

bool occupied(int x, int y) {
    return lines[y][x] == '#';
}

Grid calc_next() {
    ssize_t h = lines.size();
    ssize_t w = lines[0].size();
    Grid next;
    next.resize(lines.size());
    for (int y = 0; y < h; ++y) {
        for (int x = 0; x < w; ++x) {
            const auto &v = lines[y][x];
            int adj = 0;
            if (v == '.') {
                next[y].append('.');
                continue;
            }
            for (int dx = -1; dx < 2; ++dx) {
                for (int dy = -1; dy < 2; ++dy) if (dx || dy) {
                    int tx = x + dx;
                    int ty = y + dy;
                    // part 1
                    // if (tx < 0 || tx >= w || ty < 0 || ty >= h) continue;
                    // adj += occupied(tx, ty);
                    // part 2
                    while (tx >= 0 && tx < w && ty >= 0 && ty < h) {
                        if (chair(tx, ty)) {
                            adj += occupied(tx, ty);
                            break;
                        }
                        tx += dx;
                        ty += dy;
                    }
                }
            }
            if (v == 'L') {
                next[y].append(adj == 0 ? '#' : 'L');
            } else if (v == '#') {
                // part 1
                // next[y].append(adj >= 4 ? 'L' : '#');
                // part 2
                next[y].append(adj >= 5 ? 'L' : '#');
            }
        }
    }
    return next;
}
