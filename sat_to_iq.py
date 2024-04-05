# Function that takes an SAT score and returns the corresponding IQ score
def sat_to_iq(sat_score):
    # SAT to IQ conversion table
    conversion_table = {
        (1530, 1600): (135, 146),
        (1500, 1530): (131, 135),
        (1450, 1500): (126, 131),
        (1400, 1450): (122, 126),
        (1350, 1400): (119, 122),
        (1300, 1360): (116, 119),
        (1250, 1300): (113, 116),
        (1200, 1250): (110, 113),
        (1150, 1200): (107, 110),
        (1100, 1150): (104, 107),
        (1040, 1100): (100, 104),
        (990, 1040): (97, 100),
        (940, 990): (94, 97),
        (890, 940): (91, 94),
        (830, 890): (87, 91),
        (790, 830): (83, 87),
        (740, 790): (78, 83),
        (690, 740): (72, 78),
        (620, 690): (65, 72),
        (600, 660): (65, 67),
        (550, 600): (61, 65),
        (500, 550): (54, 61),
        (450, 500): (54, 54),
        (400, 450): (54, 54)
    }

    # Find the corresponding IQ range for the SAT score
    for (sat_range_start, sat_range_end), (iq_start, iq_end) in conversion_table.items():
        if sat_range_start <= sat_score <= sat_range_end:
            # Return the average of the IQ range
            return ((sat_score-sat_range_start)/(sat_range_end-sat_range_start)) * (iq_end-iq_start) + iq_start

    # If SAT score is out of range, return None
    return None

# Example use of the function
# Replace 'sat_score_example' with an actual SAT score to get the IQ estimate
sat_score_example = 1600
print(sat_to_iq(sat_score_example))
