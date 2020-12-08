#include <AK/Span.h>
#include <AK/StringUtils.h>
#include <AK/Vector.h>
#include <LibCore/File.h>
#include <stdio.h>

struct Instruction {
    enum class Op {
        Acc,
        Nop,
        Jmp,
    } op;
    int arg;
};

struct Pair {
    int x;
    int y;
};

Instruction parse_line(AK::String &&line) {
    auto parts = line.split_view(' ');
    Instruction ins;
    if (parts[0] == "acc") {
        ins.op = Instruction::Op::Acc;
    } else if (parts[0] == "jmp") {
        ins.op = Instruction::Op::Jmp;
    } else {
        ins.op = Instruction::Op::Nop;
    }
    ins.arg = AK::StringUtils::convert_to_int(parts[1]).value();
    return ins;
}

Pair run(const AK::Vector<Instruction> &prog) {
    int pc = 0, acc = 0;
    AK::HashTable<int> seen;
    while (pc < prog.size() && !seen.contains(pc)) {
        seen.set(pc);
        const auto &ins = prog[pc];
        switch (ins.op) {
        case Instruction::Op::Acc: acc += ins.arg; pc += 1; break;
        case Instruction::Op::Nop: pc += 1; break;
        case Instruction::Op::Jmp: pc += ins.arg; break;
        }
    }
    return {pc, acc};
}

int main(int, char**)
{
    AK::Vector<Instruction> prog;
    auto file = Core::File::construct();
    file->set_filename("input");
    file->open(Core::IODevice::OpenMode::ReadOnly);
    while (!file->eof()) {
        auto line = AK::String(ReadonlyBytes(file->read_line(128).bytes()));
        if (line.length() > 0) {
            prog.append(parse_line(AK::move(line)));
        }
    }
    auto res = run(prog);
    printf("Part 1: pc %d, acc %d\n", res.x, res.y);
    for (int i = 0; i < prog.size(); ++i) {
        if (prog[i].op != Instruction::Op::Acc) {
            auto new_prog = prog;
            auto &new_op = new_prog[i].op;
            new_op = new_op == Instruction::Op::Jmp ? Instruction::Op::Nop : Instruction::Op::Nop;
            auto res = run(new_prog);
            if (res.x >= prog.size()) {
                printf("Part 2: %d\n", res.y);
                return 0;
            }
        }
    }
    return 0;
}
