def process_comments(lines):
    processed_lines = []
    in_block_comment = False

    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('/*'):
            in_block_comment = True
            continue
        if '*/' in stripped_line:
            in_block_comment = False
            continue
        if not in_block_comment and not stripped_line.startswith('//'):
            processed_lines.append(line)

    return processed_lines
