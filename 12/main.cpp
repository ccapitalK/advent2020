#include <AK/String.h>
#include <LibCore/File.h>
#include <stdio.h>

int dir=1, x=0, y=0, x2=10, y2=1;
int sx = 0, sy = 0;
int xdirs[4] = {
    0, 1, 0, -1
};
int ydirs[4] = {
    1, 0, -1, 0
};

int main(int, char**)
{
    auto res = Core::File::open("input", Core::IODevice::OpenMode::ReadOnly);
    if (res.is_error()) {
        dbg() << "Error: " << res.error();
        return 1;
    }
    auto file = res.value();
    while (!file->eof()) {
        auto line = String(ReadonlyBytes(file->read_line(128).bytes()));
        if (!line.length()) continue;
        char d = line[0];
        auto dist = line.substring(1, line.length()-1).to_int().value();
        // Part 1
        switch (d) {
        case 'N': y += dist; break;
        case 'E': x += dist; break;
        case 'S': y -= dist; break;
        case 'W': x -= dist; break;
        case 'L': dir = (dir + (dist/90) * 3) % 4; break;
        case 'R': dir = (dir + (dist/90) * 1) % 4; break;
        case 'F': x += dist * xdirs[dir]; y += dist * ydirs[dir]; break;
        }
        // Part 2
        switch (d) {
        case 'N': y2 += dist; break;
        case 'E': x2 += dist; break;
        case 'S': y2 -= dist; break;
        case 'W': x2 -= dist; break;
        case 'L': for (int i = 0; i < dist/90; ++i) {
                int t = x2;
                x2 = -y2;
                y2 = t;
            }
            break;
        case 'R': for (int i = 0; i < dist/90; ++i) {
                int t = x2;
                x2 = y2;
                y2 = -t;
            }
            break;
        case 'F': sx += dist * x2; sy += dist * y2; break;
        }
    }
    printf("Part 1: %d\n", abs(x) + abs(y));
    printf("Part 2: %d\n", abs(sx) + abs(sy));
    return 0;
}
