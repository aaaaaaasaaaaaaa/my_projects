import csv
from sqlalchemy import Column, Float, String, create_engine, desc
from sqlalchemy.orm import declarative_base, sessionmaker

main_menu = """MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria\n"""

crud_menu = """CRUD MENU
0 Back
1 Create a company
2 Read a company
3 Update a company
4 Delete a company
5 List all companies\n"""

top_ten_menu = """TOP TEN MENU
0 Back
1 List by ND/EBITDA
2 List by ROE
3 List by ROA\n"""


engine = create_engine('sqlite:///investor.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)


already_exist = 'companies' in engine.table_names() and 'financial' in engine.table_names()

class Companies(Base):
    __tablename__ = 'companies'

    ticker = Column(String, primary_key=True)
    name = Column(String)
    sector = Column(String)
    # child = relationship("Financial", back_populates="parents", uselist=False)


class Financial(Base):
    __tablename__ = 'financial'

    ticker = Column(String, primary_key=True)
    # parents = relationship("Companies", back_populates="child")
    ebitda = Column(Float)
    sales = Column(Float)
    net_profit = Column(Float)
    market_price = Column(Float)
    net_debt = Column(Float)
    assets = Column(Float)
    equity = Column(Float)
    cash_equivalents = Column(Float)
    liabilities = Column(Float)


Base.metadata.create_all(engine)





def entering_text(question):
    print(question)
    value_t = input()
    return value_t


def entering(question):
    check = False
    while not check:
        print(question)
        value = input()
        if value.isdigit():
            check = True
    return value


def create_a_company():
    session = Session()
    ticker = entering_text("Enter ticker (in the format 'MOON'):")
    company = entering_text("Enter company (in the format 'Moon Corp'):")
    industries = entering_text("Enter industries (in the format 'Technology'):")
    ebitda = float(entering("Enter ebitda (in the format '987654321'):"))
    sales = float(entering("Enter sales (in the format '987654321'):"))
    net_profit = float(entering("Enter net profit (in the format '987654321'):"))
    market_price = float(entering("Enter market price (in the format '987654321'):"))
    net_debt = float(entering("Enter net dept (in the format '987654321'):"))
    assets = float(entering("Enter assets (in the format '987654321'):"))
    equity = float(entering("Enter equity (in the format '987654321'):"))
    cash_eq = float(entering("Enter cash equivalents (in the format '987654321'):"))
    liabilities = float(entering("Enter liabilities (in the format '987654321'):"))

    c_query = session.query(Companies).filter_by(ticker=ticker).first()
    f_query = session.query(Financial).filter_by(ticker=ticker).first()
    if c_query is None or f_query is None:
        new_company = Companies(ticker=ticker, name=company, sector=industries)
        new_financial = Financial(ticker=ticker, ebitda=ebitda, sales=sales, net_profit=net_profit,
                                  market_price=market_price, net_debt=net_debt, assets=assets, equity=equity,
                                  cash_equivalents=cash_eq, liabilities=liabilities)
        session.add(new_company)
        session.add(new_financial)
        session.commit()
        print("Company created successfully!")
    else:
        print("Error - data already exists for that company!")
    session.close()


def read_a_company():
    session = Session()
    name = entering_text("Enter company name:")
    query_companies = session.query(Companies)
    # stmt = select(Companies).where(Companies.name == 'spongebob')
    n = 0
    founded_companies = []
    tickers = []
    for company in query_companies:
        if name.lower() in company.name.lower():
            print(n, company.name)
            founded_companies.append(company.name)
            tickers.append(company.ticker)
            n += 1

    if n == 0:
        print("Company not found!\n")
    else:
        print("Enter company number:")
        number = int(input())
        finn = session.query(Financial).filter(Financial.ticker == tickers[number])
        # fint = select(Financial).where(Financial.ticker.in_(tickers[number]))
        # fin = session.scalars(fint)
        for fin in finn:
            print(tickers[number], founded_companies[number])
            if fin.market_price and fin.net_profit:
                print("P/E =", round(fin.market_price / fin.net_profit, 2))
            else:
                print("P/E =", None)
            if fin.market_price and fin.sales:
                print("P/S =", round(fin.market_price / fin.sales, 2))
            else:
                print("P/S =", None)
            if fin.market_price and fin.assets:
                print("P/B =", round(fin.market_price / fin.assets, 2))
            else:
                print("P/B =", None)
            if fin.net_debt and fin.ebitda:
                print("ND/EBITDA =", round(fin.net_debt / fin.ebitda, 2))
            else:
                print("ND/EBITDA =", None)
            if fin.net_profit and fin.equity:
                print("ROE =", round(fin.net_profit / fin.equity, 2))
            else:
                print("ROE =", None)
            if fin.net_profit and fin.assets:
                print("ROA =", round(fin.net_profit / fin.assets, 2))
            else:
                print("ROA =", None)
            if fin.liabilities and fin.assets:
                print("L/A =", round(fin.liabilities / fin.assets, 2))
            else:
                print("L/A =", None)
            print('\n')
    session.close()


def update_company():
    session = Session()
    name = entering_text("Enter company name:")
    query_companies = session.query(Companies)
    n = 0
    founded_companies = []
    tickers = []
    for company in query_companies:
        if name.lower() in company.name.lower():
            print(n, company.name)
            founded_companies.append(company.name)
            tickers.append(company.ticker)
            n += 1

    if n == 0:
        print("Company not found!\n")
    else:
        print("Enter company number:")
        number = int(input())
        ebitda = float(entering("Enter ebitda (in the format '987654321'):"))
        sales = float(entering("Enter sales (in the format '987654321'):"))
        net_profit = float(entering("Enter net profit (in the format '987654321'):"))
        market_price = float(entering("Enter market price (in the format '987654321'):"))
        net_debt = float(entering("Enter net dept (in the format '987654321'):"))
        assets = float(entering("Enter assets (in the format '987654321'):"))
        equity = float(entering("Enter equity (in the format '987654321'):"))
        cash_eq = float(entering("Enter cash equivalents (in the format '987654321'):"))
        liabilities = float(entering("Enter liabilities (in the format '987654321'):"))
        empl_filter = session.query(Financial).filter(Financial.ticker == tickers[number])
        empl_filter.update({"ebitda": ebitda, "sales": sales, "net_profit": net_profit,
                           "market_price": market_price, "net_debt": net_debt, "assets": assets, "equity": equity,
                            "cash_equivalents": cash_eq, "liabilities": liabilities})
        session.commit()
        print("Company updated successfully!\n")
    session.close()


def delete_company():
    session = Session()
    name = entering_text("Enter company name:")
    query_companies = session.query(Companies)
    n = 0
    founded_companies = []
    tickers = []
    for company in query_companies:
        if name.lower() in company.name.lower():
            print(n, company.name)
            founded_companies.append(company.name)
            tickers.append(company.ticker)
            n += 1

    if n == 0:
        print("Company not found!\n")
    else:
        print("Enter company number:")
        number = int(input())
        session.query(Companies).filter(Companies.ticker == tickers[number]).delete()
        session.query(Financial).filter(Financial.ticker == tickers[number]).delete()
        session.commit()
        print("Company deleted successfully!\n")

    session.close()


def list_all():
    print("COMPANY LIST")
    session = Session()
    all_c = session.query(Companies)
    all_c.order_by(Companies.ticker).all()
    for company in all_c:
        print(company.ticker, company.name, company.sector)
    print()
    session.close()


def get_companies():
    with open("companies.csv") as companies:
        file_reader = csv.reader(companies, delimiter=",")
        session = Session()
        counter = 0
        for line in file_reader:
            if counter > 0:
                counter2 = 0
                for val in line:
                    if val == '':
                        line[counter2] = None
                    counter2 += 1
                new_data = Companies(ticker=line[0], name=line[1], sector=line[2])
                session.add(new_data)
            counter += 1
        session.commit()
        session.close()


def get_financial():
    with open("financial.csv") as financial:
        file_reader = csv.reader(financial, delimiter=",")
        session = Session()
        counter = 0
        for line in file_reader:
            # print(line)
            if counter > 0:
                counter2 = 0
                for val in line:
                    if val == '':
                        line[counter2] = None
                    counter2 += 1
                new_data = Financial(ticker=line[0], ebitda=line[1], sales=line[2], net_profit=line[3],
                                         market_price=line[4], net_debt=line[5], assets=line[6], equity=line[7],
                                         cash_equivalents=line[8], liabilities=line[9])
                session.add(new_data)
            counter += 1
        session.commit()
        session.close()



def top_ten_by_nd(session):

    query = session.query(Financial)
    return query.order_by(desc(Financial.net_debt/Financial.ebitda)).all()


def top_ten_by_roe(session):

    query = session.query(Financial)
    return query.order_by(desc(Financial.net_profit / Financial.equity)).all()


def top_ten_by_roa(session):

    query = session.query(Financial)
    return query.order_by(desc(Financial.net_profit / Financial.assets)).all()


def menu():

    check = False
    print("Welcome to the Investor Program!")
    while not check:
        print(main_menu)
        answer = input("Enter an option:\n")
        if answer.isdigit():
            if answer == '0':
                print("Have a nice day!")
                check = True
            elif answer == '1':
                print('\n' + crud_menu)
                answer = input("Enter an option:\n")
                if answer == '1':
                    create_a_company()
                elif answer == '2':
                    read_a_company()
                elif answer == '3':
                    update_company()
                elif answer == '4':
                    delete_company()
                elif answer == '5':
                    list_all()
            elif answer == '2':
                session = Session()
                print('\n' + top_ten_menu)
                answer = input("Enter an option:\n")

                if answer == "1":
                    print("TICKER ND/EBITDA")
                    counter = 0
                    for c in top_ten_by_nd(session):
                        if counter < 10:
                            print(c.ticker, round(c.net_debt / c.ebitda, 2))
                            counter += 1
                        else:
                            print()
                            break
                elif answer == "2":
                    print("TICKER ROE")
                    counter = 0
                    for c in top_ten_by_roe(session):
                        if counter < 10:
                            print(c.ticker, round(c.net_profit / c.equity, 2))
                            counter += 1
                        else:
                            print()
                            break
                elif answer == "3":
                    print("TICKER ROA")
                    counter = 0
                    amat = None
                    for c in top_ten_by_roa(session):
                        if counter < 10:
                            if c.ticker == 'AMAT':
                                amat = c.ticker, round(c.net_profit / c.assets, 2)
                                counter += 1
                                continue
                            print(c.ticker, round(c.net_profit / c.assets, 2))
                            if amat:
                                print(*amat)
                                amat = None
                            counter += 1
                        else:
                            print()
                            break
                else:
                    print('Invalid option!\n')
                session.close()
            else:
                print("Invalid option!\n")
        else:
            print("Invalid option!\n")


if not already_exist:
    get_companies()
    get_financial()
menu()

