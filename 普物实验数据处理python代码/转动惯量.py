# import math

# # Define the formula as a function
# def calculate_beta(k_m, k_n, t_m, t_n):
#     return (2 * math.pi * (k_n * t_m - k_m * t_n)) / (t_n**2 * t_m - t_m**2 * t_n)

# # Given values for k_m, k_n, t_m, t_n in the 9 sets
# values = [
#     ########################1
#     # (1, 2, 0.8947, 1.8017),
#     # (2, 3, 1.8017, 2.7277),
#     # (3, 4, 2.7277, 3.6667),
#     # (4, 5, 3.6667, 4.6259),
#     # (5, 6, 4.6259, 5.5996),
#     # (6, 7, 5.5996, 6.5944),
#     # (7, 8, 6.5944, 7.6043),
#     # (8, 9, 7.6043, 8.6373),
#     # (9, 10, 8.6373, 9.6873),
#     #########################2
#     # (1, 2, 1.2157, 1.9577),
#     # (2, 3, 1.9577, 2.5474),
#     # (3, 4, 2.5474, 3.0498),
#     # (4, 5, 3.0498, 3.4975),
#     # (5, 6, 3.4975, 3.9035),
#     # (6, 7, 3.9035, 4.2798),
#     # (7, 8, 4.2798, 4.6301),
#     # (8, 9, 4.6301, 4.9754),
#     # (9, 10,4.9754, 5.3210),
#     #########################3
#     # (1, 2, 0.9917, 1.9994),
#     # (2, 3, 1.9994, 3.0152),
#     # (3, 4, 3.0152, 4.0473),
#     # (4, 5, 4.0473, 5.0877),
#     # (5, 6, 5.0877, 6.1450),
#     # (6, 7, 6.1450, 7.2114),
#     # (7, 8, 7.2114, 8.2953),
#     # (8, 9, 8.2953, 9.3891),
#     # (9, 10,9.3891, 10.5015),
#     #########################4
#     # (1, 2, 1.6001, 2.6019),
#     # (2, 3, 2.6019, 3.4018),
#     # (3, 4, 3.4018, 4.0848),
#     # (4, 5, 4.0848, 4.6943),
#     # (5, 6, 4.6943, 5.2468),
#     # (6, 7, 5.2468, 5.7592),
#     # (7, 8, 5.7592, 6.2369),
#     # (8, 9, 6.2369, 6.7098),
#     # (9, 10,6.7098, 7.1829),
#     #########################5
#     # (1, 2, 1.3931, 2.8139),
#     # (2, 3, 2.8139, 4.2723),
#     # (3, 4, 4.2723, 5.7594),
#     # (4, 5, 5.7594, 7.2874),
#     # (5, 6, 7.2874, 8.8479),
#     # (6, 7, 8.8479, 10.4584),
#     # (7, 8, 10.4584, 12.1126),
#     # (8, 9, 12.1126, 13.8201),
#     # (9, 10,13.8201, 15.5719),
#     #########################6
#     (1, 2, 1.5086, 2.4459),
#     (2, 3, 2.4459, 3.1870),
#     (3, 4, 3.1870, 3.8239),
#     (4, 5, 3.8239, 4.3877),
#     (5, 6, 4.3877, 4.9023),
#     (6, 7, 4.9023, 5.3758),
#     (7, 8, 5.3758, 5.8195),
#     (8, 9, 5.8195, 6.2371),
#     (9, 10,6.2371, 6.6525),
# ]

# # Calculate beta for each set of values
# beta_values = [calculate_beta(k_m, k_n, t_m, t_n) for k_m, k_n, t_m, t_n in values]

# # Print out the list of beta values
# print(beta_values)




def calculate_J_values(m_val, R_val, g_val, beta_1_val, beta_2_val, beta_3_val, beta_4_val):
    # Calculate J1
    J_1_val = R_val * m_val * (g_val - R_val * beta_2_val) / (beta_2_val - beta_1_val)
    # Calculate J2
    J_2_val = R_val * m_val * (g_val - R_val * beta_4_val) / (beta_4_val - beta_3_val)
    # Calculate J3
    J_3_val = J_2_val - J_1_val
    
    return J_1_val, J_2_val, J_3_val

# Example calculation with assumed default values
print(calculate_J_values(m_val=0.0392, R_val=0.03, g_val=9.7940, beta_1_val=-0.0610, beta_2_val=1.5998, beta_3_val=-0.03335, beta_4_val=1.0217))

# Define the function to calculate J and the relative error E based on given or default values for R_outer and R_inner.

def calculate_J_and_error(J_3_val, m_val, R_outer_val=0.119705, R_inner_val=0.105195):
    # Calculate J
    J_val = (m_val / 2) * (R_outer_val**2 + R_inner_val**2)
    
    # Calculate the relative error E
    E_val = ((J_3_val - J_val) / J_val) * 100
    
    return J_val, E_val

# Using the previously calculated J_3 value (assuming it's the correct one from the earlier calculation)
J_3_value_from_previous_calculation = 0.00599188029974115

# Example calculation with default values for R_outer and R_inner
print(calculate_J_and_error(J_3_value_from_previous_calculation, m_val=0.4265))
