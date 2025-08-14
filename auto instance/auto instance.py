import re
import sys

def parse_verilog_module(verilog_code):
    """
    Verilog 모듈 정의 코드에서 모듈 이름과 포트 정보(벡터 포함)를 추출합니다.
    """
    module_match = re.search(r'module\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', verilog_code)
    if not module_match:
        return None, None
    module_name = module_match.group(1)

    port_regex = re.compile(
        r'(input|output|inout)\s+'
        r'(?:reg|wire)?\s*'
        r'(\[.*?\])?\s*'
        r'([a-zA-Z_][a-zA-Z0-9_]*)'
        , re.MULTILINE)
    ports = port_regex.findall(verilog_code)
    return module_name, ports

def generate_verilog():
    """
    한 번의 Verilog 코드 생성 작업을 수행하는 함수.
    """
    print("\n📋 Verilog 모듈 정의 코드를 아래에 붙여넣으세요.")
    print("   입력이 끝나면 새 줄에서 'EOF'를 입력하거나,")
    print("   [Ctrl+D] (Linux/macOS) 또는 [Ctrl+Z + Enter] (Windows)를 누르세요.")
    print("-" * 50)
    
    user_code = sys.stdin.read()

    if not user_code.strip():
        print("\n❌ 입력된 코드가 없습니다. 처음으로 돌아갑니다.")
        return

    module_name, ports = parse_verilog_module(user_code)

    if not module_name or not ports:
        print("\n❌ 유효한 Verilog 모듈 정의를 찾을 수 없습니다. 처음으로 돌아갑니다.")
        return

    print(f"\n✅ 모듈 '{module_name}'을(를) 성공적으로 분석했습니다.")
    print("-" * 50)

    # 인스턴스 이름 입력
    instance_name = ""
    while not instance_name:
        instance_name = input("▶️ 생성할 인스턴스화 이름(Instance Name)을 입력하세요: ")

    # 연결 모드 선택
    mode = ""
    while mode not in ['1', '2']:
        print("\n▶️ 연결 방식을 선택하세요:")
        print("   1. 직접 입력 모드")
        print("   2. 자동 생성 모드 ('w_' 접두사)")
        mode = input(">> 선택 (1 또는 2): ")

    connections = []
    max_port_len = max(len(p[2]) for p in ports) if ports else 0

    if mode == '1':
        print("\n🔗 [직접 입력 모드] 각 포트에 연결할 wire/reg 이름을 입력하세요.")
        for direction, vector, port_name in ports:
            vector_str = (vector + " ") if vector else ""
            prompt = f"  ({direction:^6}) {vector_str}{port_name.ljust(max_port_len)} : "
            wire_name = input(prompt)
            connections.append({'port': port_name, 'wire': wire_name, 'vector': vector})
            
    elif mode == '2':
        print("\n🔗 [자동 생성 모드] 'w_' 접두사를 붙여 자동 생성합니다.")
        for direction, vector, port_name in ports:
            wire_name = f"w_{port_name}"
            connections.append({'port': port_name, 'wire': wire_name, 'vector': vector})
        print("   ...자동 생성이 완료되었습니다.")

    print("\n" + "=" * 50)
    print("🎉 완성된 Verilog 코드 🎉")
    print("=" * 50)
    
    # Wire 선언부 생성 및 정렬
    print("// Wire & Reg Declarations")
    max_decl_width = 0
    for conn in connections:
        vector_str = (conn['vector'] + " ") if conn['vector'] else ""
        current_width = len(f"wire {vector_str}")
        if current_width > max_decl_width:
            max_decl_width = current_width
            
    for conn in connections:
        vector_str = (conn['vector'] + " ") if conn['vector'] else ""
        declaration_part = f"wire {vector_str}"
        aligned_declaration = declaration_part.ljust(max_decl_width)
        print(f"{aligned_declaration}{conn['wire']};")
    
    print()

    # 모듈 인스턴스화 부분 생성
    print(f"// Module Instantiation for {module_name}")
    print(f"{module_name} {instance_name} (")
    num_connections = len(connections)
    for i, conn in enumerate(connections):
        aligned_port = f".{conn['port']}".ljust(max_port_len + 2)
        comma = "," if i < num_connections - 1 else ""
        print(f"    {aligned_port}({conn['wire']}){comma}")
    print(");")
    print("-" * 50)

def main():
    """
    메인 함수: 프로그램을 무한 반복하며, 사용자 요청 시 종료.
    """
    while True:
        generate_verilog() # 핵심 기능 함수 호출
        
        # 사용자에게 계속할지 묻기
        print("\n✅ 작업 완료!")
        choice = input("새로운 코드를 생성하려면 Enter를, 프로그램을 종료하려면 'exit' 또는 'q'를 입력하세요: ").lower()
        
        if choice in ['exit', 'q', '종료', '나가기']:
            print("\n프로그램을 종료합니다.")
            break # 무한 반복문 탈출

if __name__ == "__main__":
    main()
