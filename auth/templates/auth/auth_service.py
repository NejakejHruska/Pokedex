from data_uzivatele import uzivatele


class AuthService:
    def __init__(self, uzivatele):
        self.__uzivatele = uzivatele

    def najdi_uzivatele(self, email):
        for uzivatele in self.__uzivatele:
            if uzivatele.email == email:
                return uzivatele

        return None

    def prihlas(self, email, heslo):
        uzivatele self.najdi_uzivatele(email):

        if uzivatele is None:
            return None
