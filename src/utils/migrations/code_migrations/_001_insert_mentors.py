from db.mentor import insert

def migrate(db):
    # test mentors
    insert(
        db=db,
        first_name="mentor1",
        last_name="smith",
        email="smith1@gmail.com",
        phone="12341234",
        address="12341234 smith st.",
        specialization="Designer",
        experience_years="10",
        bio="I am a designer",
    )
    insert(
        db=db,
        first_name="mentor2",
        last_name="smith",
        email="smith2@gmail.com",
        phone="12341235",
        address="a smith st.",
        specialization="Receptionist",
        experience_years="104",
        bio="I am barely alive",
    )
    insert(
        db=db,
        first_name="mentor2",
        last_name="smith",
        email="smith2@gmail.com",
        phone="12341235",
        address="a smith st.",
        specialization="Receptionist",
        experience_years="104",
        bio="I am barely alive",
    )
    insert(
        db=db,
        first_name="mentor2",
        last_name="smith",
        email="smith2@gmail.com",
        phone="12341235",
        address="a smith st.",
        specialization="Receptionist",
        experience_years="104",
        bio="I am barely alive",
    )