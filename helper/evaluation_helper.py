"""

Helper functions for evaluation of audit results

"""


def evaluation(df):
    df['is_correct'] = df['user_answer'].str.upper() == df['correct_answer'].str.upper()
    correct_count = df['is_correct'].sum()
    total_questions = len(df)
    accuracy = round((correct_count / total_questions) * 100, 2)

    return correct_count, accuracy
