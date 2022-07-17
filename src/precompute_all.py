"""
    Finds top questions for all keywords and stores them in the keyword_pages.question table.

    Runtime:
    100%|█████████████████████████████████████████████████████████| 82685/82685 [14:29:28<00:00,  1.58it/s]
"""
import sys
sys.path.append('..')

from website_db_connect import db

from main import get_top_questions

from tqdm import tqdm
import json


if __name__ == '__main__':
    cur = db.cursor()

    cur.execute("""
    SELECT id, name 
    FROM keyword

    WHERE name IN (
        "computer architecture",
        "case-based reasoning"
    )
    """)
    keyword_ts = cur.fetchall()


    # Insert into 'question' table
    pbar = tqdm(total=len(keyword_ts))
    num_complete = 0

    for kw_id, keyword in keyword_ts:
        res = get_top_questions(keyword)

        print(keyword, '---', len(res))
        for q in res:
            cur.execute(
                "INSERT INTO question (keyword_id, content) VALUES (%s, %s)", 
                [kw_id, q]
            )

        num_complete += 1
        pbar.update(1)

        if num_complete % 150 == 0:
            db.commit()
    

    db.commit()
    pbar.close()
