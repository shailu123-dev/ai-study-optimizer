def calculate_score(total_reward, focus_level, energy_level):
    score = 0.0

    # 🎯 reward contribution
    score += total_reward / 20

    # 📈 focus bonus
    score += focus_level / 100 * 0.3

    # ⚡ energy balance
    if energy_level > 40:
        score += 0.2
    else:
        score -= 0.2

    # 🔒 clamp score
    score = max(0.0, min(1.0, score))

    return round(score, 2)