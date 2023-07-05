from aiogram.dispatcher.filters.state import StatesGroup, State


class SellerState(StatesGroup):
    WaitForNewUser = State()
    WaitForEmploymentType = State()
    WaitForPersonInfo = State()
    WaitForINN = State()
    WaitForPaymentDetails = State()
    WaitForLogo = State()
    WaitForExperienceDescription = State()
    WaitForPortfolio = State()
    WaitForGuaranteesDescription = State()
    WaitForConfidentialityInfo = State()


class OrderState(StatesGroup):
    WaitForOrder = State()
    WaitForDescription = State()
    WaitForSample = State()
    WaitForQuantity = State()
    WaitForLength = State()
    WaitForWidth = State()
    WaitForHeight = State()
    WaitForMaterial = State()
    WaitForColor = State()
    WaitForPostProcessing = State()
    WaitForAcceptance = State()
    WaitForLastState = State()
    # WaitForDetails = State()
    # WaitForPickup = State()
    # WaitForPayment = State()