def create_users_table():
    return """CREATE TABLE Users(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            gender TEXT NOT NULL,
            birthDate TIMESTAMP NOT NULL,
            weight REAL,
            hasDiseases BOOLEAN,
            lastTreatmentDate TIMESTAMP,
            bloodClass TEXT,
            lastDonationDate TIMESTAMP DEFAULT '1970-01-01 00:00:00',
            nextDonationDate TIMESTAMP DEFAULT '1970-01-01 00:00:00'
            )"""

# -------------------------------------


def create_governorates_table():
    return """CREATE TABLE Governorates(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
            )"""

# -------------------------------------


def create_cities_table():
    return """CREATE TABLE Cities(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            governorateId INT NOT NULL REFERENCES Governorates(id)
            )"""

# -------------------------------------


def create_blood_banks_table():
    return """CREATE TABLE BloodBanks(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            street TEXT NOT NULL,
            cityId INT NOT NULL REFERENCES Cities(id),
            phone TEXT,
            info TEXT,
            createdAt TIMESTAMP NOT NULL
            )"""

# -------------------------------------


def create_hospitals_table():
    return """CREATE TABLE Hospitals(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            phone TEXT,
            street TEXT NOT NULL,
            cityId INT NOT NULL REFERENCES Cities(id),
            info TEXT,
            createdAt TIMESTAMP NOT NULL
            )"""

# -------------------------------------


def create_orders_table():
    return """CREATE TABLE Orders (
            id SERIAL PRIMARY KEY,
            bloodBankId INT NOT NULL REFERENCES BloodBanks(id),
            hospitalId INT NOT NULL REFERENCES Hospitals(id),
            amount INT NOT NULL,
            bloodClass TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending',
            date TIMESTAMP NOT NULL,
            type TEXT NOT NULL
            )"""

# -------------------------------------


def create_blood_cases_table():
    return """CREATE TABLE BloodCases(
            id INT PRIMARY KEY NOT NULL,
            bloodBankId INT NOT NULL REFERENCES BloodBanks(id),
            orderId INT REFERENCES Orders(id),
            type TEXT NOT NULL,
            bloodClass TEXT NOT NULL,
            storingDate TIMESTAMP NOT NULL,
            expirationDate TIMESTAMP NOT NULL,
            isDeleted boolean not null default false
            )"""

# -------------------------------------


def create_donations_table():
    return """CREATE TABLE Donations(
            id SERIAL PRIMARY KEY,
            userId INT NOT NULL REFERENCES Users(id),
            bloodBankId INT NOT NULL REFERENCES BloodBanks(id),
            status TEXT NOT NULL DEFAULT 'pending',
            donationDate TIMESTAMP,
            bags INT,
            createdAt TIMESTAMP NOT NULL,
            bloodType TEXT NOT NULL DEFAULT 'complete'
            )"""

# -------------------------------------
