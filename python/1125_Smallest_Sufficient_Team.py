class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        num_of_people = len(people)
        num_of_skills = len(req_skills)
        skill_id = {}
        for i, skill in enumerate(req_skills):
            skill_id[skill] = i

        skills_mask_of_person = [0] * num_of_people
        for i in range(num_of_people):
            for skill in people[i]:
                skills_mask_of_person[i] |= 1 << skill_id[skill]

        dp = [-1] * (1 << num_of_skills)
        dp[0] = 0

        def f(skills_mask):
            if dp[skills_mask] != -1:
                return dp[skills_mask]
            for i in range(num_of_people):
                new_skills_mask = skills_mask & ~skills_mask_of_person[i]
                if new_skills_mask != skills_mask:
                    people_mask = f(new_skills_mask) | (1 << i)
                    if (dp[skills_mask] == -1 or
                        people_mask.bit_count()
                       < dp[skills_mask].bit_count()):
                        dp[skills_mask] = people_mask
            return dp[skills_mask]
        answer_mask = f((1 << num_of_skills) - 1)
        team = []
        for i in range(num_of_people):
            if (answer_mask >> i) & 1:
                team.append(i)
        return team
