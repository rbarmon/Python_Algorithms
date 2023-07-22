if __name__ == "__main__":
    def test_edge_case_duplicate_check(self):
        occupancy_probability = [
            [57, 76, 38, 22],
            [56, 94, 54, 68],
            [71, 86, 86, 99],
            [81, 0, 0, 60],
            [36, 22, 43, 93]
        ]
        expec_res_1 = [184, [(0, 3), (1, 2), (2, 1), (3, 1), (4, 1)]]
        expec_res_2 = [184, [(0, 3), (1, 2), (2, 2), (3, 2), (4, 1)]]
        my_res = select_sections(occupancy_probability)
        self.assertTrue(my_res == expec_res_1 or my_res == expec_res_2)