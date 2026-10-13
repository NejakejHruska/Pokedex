class User:
    def __innit__(self, jmeno, prijmeni, email, nickname, role='uzivatel'):
        self.id = id
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.email = email
        self.nickname = nickname
        self.role = role
        self.__aktivni = True

    def cele_jmeno(self):
        return f'{self.jmeno} {self.prijmeni}'

    def je_admin(self):
        return self.role == 'admin'

    def je_aktivni(self):
        return self.__aktivni

    def deaktivo(self):
        return self.__aktivni == False