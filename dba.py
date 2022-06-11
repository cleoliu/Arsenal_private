import uuid

from sqlalchemy import create_engine, text, Integer, Column, String, ForeignKey, select, func, DateTime, Text, Boolean, \
    BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Session
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship

mapper_registry = registry()
Base = mapper_registry.generate_base()


class Organization(Base):
    __tablename__ = 'organization'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    account_id = Column(UUID, server_default=text("gen_random_uuid()"), unique=True)
    org_name = Column(String(255), unique=True)
    phone = Column(String(100), nullable=True)
    tax_id = Column(String(100), nullable=True)
    country = Column(String(100), nullable=True)
    address = Column(String(1024), nullable=True)
    estimate_tester = Column(Integer, default=1)
    actual_tester = Column(Integer, default=1)
    estimate_viewer = Column(Integer, default=0)
    actual_viewer = Column(Integer, default=0)
    allow_project = Column(Integer, default=1)
    allow_group = Column(Integer, default=1)
    allow_case_per_group = Column(Integer, default=50)
    allow_run = Column(Integer, default=1)
    account_type = Column(Integer, default=0)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    users = relationship("OrgUser", back_populates="organize")


class OrgUser(Base):
    __tablename__ = 'org_user'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(UUID, server_default=text("gen_random_uuid()"), unique=True)
    user_mail = Column(String(255), unique=True)
    user_name = Column(String(30))
    password = Column(String(30))
    role = Column(Integer, default=0)  # 0 = viewer
    avatar_url = Column(Text, nullable=True)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    last_login_date = Column(DateTime(timezone=True), onupdate=func.now())
    status = Column(Boolean, default=True)
    org_id = Column(UUID, ForeignKey('organization.account_id'))
    organize = relationship("Organization", back_populates="users")

#
# class CaseGroupModel(Base):
#     __tablename__ = 'case_group'
#     id = Column(String(50), primary_key=True, server_default=text("gen_random_uuid()"))
#     case_group_id = Column(String(50), server_default=text("gen_random_uuid()"), unique=True)
#     case_group_name = Column(String(30), unique=False)
#     sections_num = Column(Integer, default=0)
#     cases_num = Column(Integer, default=0)
#     description = Column(Text, nullable=True)
#     org_id = Column(UUID, ForeignKey('organization.account_id'))


class CaseGroupModel(Base):
    __tablename__ = 'group_table'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    group_id = Column(UUID, server_default=text("gen_random_uuid()"), unique=True)
    group_name = Column(String(30), unique=False)
    description = Column(Text, nullable=True)
    creator = Column(String(255), unique=True)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    org_id = Column(UUID, ForeignKey('organization.account_id'))


write_engine = create_engine('postgresql://postgres:keenlity@180.218.211.203:8197/postgres', echo=True, future=True)
read_engine = create_engine('postgresql://postgres:keenlity@180.218.211.203:8197/postgres', echo=True, future=True)
engines = {
    'write': write_engine,
    'read': read_engine
}
mapper_registry.metadata.create_all(write_engine)


class Engines(object):

    def __init__(self):
        self.engines = engines

    def get_write(self):
        return self.engines.get('write')

    def get_read(self):
        return self.engines.get('read')






if __name__ == '__main__':
    engine_instance = Engines()
    engine = engine_instance.get_read()

    with Session(engine) as session:
        statement = select(OrgUser).where(OrgUser.user_mail == "fabianlin@keenlity.com")
        result = session.execute(statement)
        print(result)
        user = result.scalar_one()
    write_engine = engine_instance.get_read()
    with Session(write_engine) as session:
        group = CaseGroupModel(org_id=user.org_id, case_group_name="test", description="testtest")
        session.add(group)
        session.commit()



    # keenlity = Organization(org_name="KEENLITY Inc.")
    # fabian = OrgUser(user_name="Fabian Lin", password="qaqaqa", user_mail="fabianlin@keenlity.com")
    # vicky = OrgUser(user_name="Vicky Yang", password="qaqaqa", user_mail="vicky@keenlity.com")
    #
    # engine_instance = Engines()
    # engine = engine_instance.get_write()
    # with Session(engine) as session:
    #     result = session.add(keenlity)
    #     session.commit()
    #     keenlity.users.append(fabian)
    #     keenlity.users.append(vicky)
    #     print(session.new)
    #     session.commit()








# class User(Base):
#     __tablename__ = 'user_account'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(30))
#     fullname = Column(String)
#
#     addresses = relationship("Address", back_populates="user")
#
#     def __repr__(self):
#         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
#
#
# class Address(Base):
#     __tablename__ = 'address'
#
#     id = Column(Integer, primary_key=True)
#     email_address = Column(String, nullable=False)
#     user_id = Column(Integer, ForeignKey('user_account.id'))
#     user = relationship("User", back_populates="addresses")