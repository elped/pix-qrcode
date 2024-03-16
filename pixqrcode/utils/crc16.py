def crc16(buf: bytes):
    crc = 0xFFFF
    polynomial = 0x1021

    for byte in buf:
        crc ^= (byte << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ polynomial
            else:
                crc <<= 1

    return crc & 0xFFFF
