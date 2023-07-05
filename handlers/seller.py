from loader import db, dp
from aiogram import types
from messages import *
from states import SellerState
from aiogram.dispatcher import FSMContext
from validators.seller import *
from aiogram import Dispatcher


@dp.callback_query_handler(text="i_am_seller", state='*')
async def welcome_seller(call: types.callback_query, state: FSMContext):
    seller_id = call.message.from_user.id
    if not db.check_seller_exists(seller_id):
        db.add_seller(seller_id)
    async with state.proxy() as data:
        data['seller_id'] = seller_id
    await SellerState.WaitForEmploymentType.set()
    await call.message.reply(GET_EMPLOYMENT_TYPE_TEXT)


@dp.message_handler(state=SellerState.WaitForEmploymentType)
async def get_employment_type(message: types.Message, state: FSMContext):
    employment_type = message.text
    try:
        async with state.proxy() as data:
            data['employment_type'] = validate_employment_type(
                data=employment_type,
                error_message=INCORRECT_EMPLOYMENT_TEXT
            )
    except (Exception, ValueError) as error:
        await message.reply(INCORRECT_EMPLOYMENT_TEXT)
    else:
        await SellerState.WaitForPersonInfo.set()
        await message.reply(GET_PERSON_INFO_TEXT)


@dp.message_handler(state=SellerState.WaitForPersonInfo)
async def get_person_info(message: types.Message, state: FSMContext):
    person_info = message.text
    try:
        async with state.proxy() as data:
            data['person_info'] = validate_person_info(
                data=person_info,
                employment_type=data.get('employment_type'),
                error_message=INCORRECT_PERSON_INFO
            )
    except Exception:
        await message.reply(INCORRECT_PERSON_INFO)
    else:
        await SellerState.WaitForINN.set()
        await message.reply(GET_INN_TEXT)


@dp.message_handler(state=SellerState.WaitForINN)
async def get_inn(message: types.Message, state: FSMContext):
    inn = message.text
    try:
        async with state.proxy() as data:
            data['inn'] = validate_inn(
                data=inn,
                error_message=INCORRECT_INN
            )
    except Exception:
        await message.reply(INCORRECT_INN)
    else:
        await SellerState.WaitForPaymentDetails.set()
        await message.reply(GET_PAYMENT_DETAILS_TEXT)

# 20 цифр
@dp.message_handler(state=SellerState.WaitForPaymentDetails)
async def get_payment_details(message: types.Message, state: FSMContext):
    payment_details = message.text
    async with state.proxy() as data:
        data['payment_details'] = payment_details
    await SellerState.WaitForLogo.set()
    await message.reply(GET_LOGO_TEXT)


@dp.message_handler(
        content_types=types.ContentType.PHOTO,
        state=SellerState.WaitForLogo
    )
async def get_logo(message: types.Message, state: FSMContext):
    logo = message.photo[-1].file_unique_id
    async with state.proxy() as data:
        data['logo'] = logo
    await SellerState.WaitForExperienceDescription.set()
    await message.reply(GET_EXPERIENCE_DESCRIPTION_TEXT)


@dp.message_handler(state=SellerState.WaitForExperienceDescription)
async def get_experience(message: types.Message, state: FSMContext):
    experience = message.text
    async with state.proxy() as data:
        data['experience'] = experience
    await SellerState.WaitForPortfolio.set()
    await message.reply(GET_PORTFOLIO_TEXT)


@dp.message_handler(state=SellerState.WaitForPortfolio)
async def get_portfolio(message: types.Message, state: FSMContext):
    portfolio_link = message.text
    async with state.proxy() as data:
        data['portfolio_link'] = portfolio_link
    await SellerState.WaitForGuaranteesDescription.set()
    await message.reply(GET_GUARANTEES_TEXT)


@dp.message_handler(state=SellerState.WaitForGuaranteesDescription)
async def get_guarantees(message: types.Message, state: FSMContext):
    guarantees = message.text
    async with state.proxy() as data:
        data['guarantees'] = guarantees
    await SellerState.WaitForConfidentialityInfo.set()
    await message.reply(GET_CONFIDENTIALITY_TEXT)


@dp.message_handler(state=SellerState.WaitForConfidentialityInfo)
async def get_confidentiality(message: types.Message, state: FSMContext):
    confidentiality = message.text
    async with state.proxy() as data:
        data['confidentiality'] = confidentiality
        id = data.get('seller_id')
        data.pop('seller_id')
        db.save_seller_info(id, data)
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(
        welcome_seller,
        commands=['register'],
        state='*'
    )
    dp.register_message_handler(
        get_employment_type,
        state=SellerState.WaitForEmploymentType
    )
    dp.register_message_handler(
        get_person_info,
        state=SellerState.WaitForPersonInfo
    )
    dp.register_message_handler(
        get_inn,
        state=SellerState.WaitForINN
    )
    dp.register_message_handler(
        get_payment_details,
        state=SellerState.WaitForPaymentDetails
    )
    dp.register_message_handler(
        get_logo,
        content_types=types.ContentType.PHOTO,
        state=SellerState.WaitForLogo
    )
    dp.register_message_handler(
        get_experience,
        state=SellerState.WaitForExperienceDescription
    )
    dp.register_message_handler(
        get_portfolio,
        state=SellerState.WaitForPortfolio
    )
    dp.register_message_handler(
        get_guarantees,
        state=SellerState.WaitForGuaranteesDescription
    )
    dp.register_message_handler(
        get_confidentiality,
        state=SellerState.WaitForConfidentialityInfo
    )
