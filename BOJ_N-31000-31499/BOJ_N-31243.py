def main():
    dur = []
    for _ in range(3):
        h_s, m_s, h_e, m_e = map(int, input().split())

        t1, t2 = h_s*60 + m_s, h_e*60 + m_e
        if t2 < t1:
            t2 += 24 * 60

        dur.append(t2 - t1)

    dur_min, dur_max = min(dur), max(dur)
    print(f"{dur_min // 60}:{dur_min % 60:02d}")
    print(f"{dur_max // 60}:{dur_max % 60:02d}")


if __name__ == "__main__":
    main()
