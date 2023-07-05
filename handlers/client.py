from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from keyboards import acceptance_keyboard
from aiogram.types import ContentType

from keyboards import *
from loader import db, dp
from messages import *
from states import OrderState
from validators.order import *


@dp.callback_query_handler(text="i_am_client", state='*')
async def make_order(call: types.CallbackQuery, state: FSMContext):
    user_id = call.message.from_user.id
    if not db.user_exists(user_id):
        db.add_user(user_id)
    order_id = db.add_order(user_id)
    async with state.proxy() as data:
        data['order_id'] = order_id
    await OrderState.WaitForDescription.set()
    await call.message.reply(GET_DESCRIPTION_TEXT)


@dp.message_handler(state=OrderState.WaitForDescription)
async def get_description(message: types.Message, state: FSMContext):
    description = message.text
    async with state.proxy() as data:
        data['description'] = description
    await OrderState.WaitForSample.set()
    await message.reply(GET_SAMPLE_TEXT)


@dp.message_handler(
        content_types=types.ContentType.PHOTO, 
        state=OrderState.WaitForSample
    )
async def get_sample(message: types.Message, state: FSMContext):
    image_id = message.photo[-1].file_unique_id
    async with state.proxy() as data:
        data['image_id'] = image_id
    await OrderState.WaitForQuantity.set()
    await message.reply(GET_QUANTITY_TEXT)


@dp.message_handler(state=OrderState.WaitForQuantity)
async def get_quantity(message: types.Message, state: FSMContext):
    quantity = message.text
    try:
        async with state.proxy() as data:
            data['quantity'] = validate_numeric_field(
                data=quantity,
                type='int',
                error_message=INCORRECT_QUANTITY_TEXT
            )     
    except (Exception, ValueError) as error:
        await message.reply(INCORRECT_QUANTITY_TEXT)
    else:
        await OrderState.WaitForLength.set()
        await message.reply(GET_LENGTH_TEXT)


@dp.message_handler(state=OrderState.WaitForLength)
async def get_length(message: types.Message, state: FSMContext):
    length = message.text
    try:
        async with state.proxy() as data:
            data['length'] = validate_numeric_field(
                data=length,
                type='float',
                error_message=INCORRECT_SIZE_TEXT
            )
    except (Exception, ValueError) as error:
        await message.reply(INCORRECT_SIZE_TEXT)
    else:
        await OrderState.WaitForWidth.set()
        await message.reply(GET_WIDTHH_TEXT)


@dp.message_handler(state=OrderState.WaitForWidth)
async def get_width(message: types.Message, state: FSMContext):
    width = message.text
    try:
        async with state.proxy() as data:
            data['width'] = validate_numeric_field(
                data=width,
                type='float',
                error_message=INCORRECT_SIZE_TEXT
            )
    except (Exception, ValueError) as error:
        await message.reply(INCORRECT_SIZE_TEXT)
    else:
        await OrderState.WaitForHeight.set()
        await message.reply(GET_HEIGHT_TEXT)


@dp.message_handler(state=OrderState.WaitForHeight)
async def get_height(message: types.Message, state: FSMContext):
    height = message.text
    try:
        async with state.proxy() as data:
            data['height'] = validate_numeric_field(
                data=height,
                type='float',
                error_message=INCORRECT_SIZE_TEXT
            )
    except (Exception, ValueError) as error:
        await message.reply(INCORRECT_SIZE_TEXT)
    else:
        await OrderState.WaitForMaterial.set()
        await message.reply(GET_MATERIAL_TEXT)


@dp.message_handler(state=OrderState.WaitForMaterial)
async def get_material(message: types.Message, state: FSMContext):
    material = message.text
    try:
        async with state.proxy() as data:
            data['material'] = validate_string_field(
                data=material,
                value_list=MATERIAL_LIST,
                error_message=INCORRECT_MATERIAL_TEXT
            )
    except (Exception, IndexError) as error:
        await message.reply(INCORRECT_MATERIAL_TEXT)
    else:
        await OrderState.WaitForColor.set()
        await message.reply(GET_COLOR_TEXT)


@dp.message_handler(state=OrderState.WaitForColor)
async def get_color(message: types.Message, state: FSMContext):
    color = message.text
    try:
        async with state.proxy() as data:
            data['color'] = validate_string_field(
                data=color,
                value_list=COLOR_LIST,
                error_message=INCORRECT_COLOR_TEXT
            )
    except (Exception, IndexError) as error:
        await message.reply(INCORRECT_COLOR_TEXT)
    else:
        await OrderState.WaitForPostProcessing.set()
        await message.reply(GET_POST_PROCESSING_TEXT)


@dp.message_handler(state=OrderState.WaitForPostProcessing)
async def get_post_processing(message: types.Message, state: FSMContext):
    post_processing = message.text
    try:
        async with state.proxy() as data:
            data['post_processing'] = validate_post_processing(
                data=post_processing,
                error_message=INCORRECT_POST_PROCESSING_TEXT
            )
            general_text = GENERAL_ORDERS_INFO_TEXT.format(
                id=data.get('id'),
                description=data.get('description'),
                quantity=data.get('quantity'),
                length=data.get('length'),
                width=data.get('width'),
                height=data.get('height'),
                material=data.get('material'),
                color=data.get('color'),
                post_processing=data.get('post_processing')
            )
    except (Exception, ValueError) as error:
        await message.reply(INCORRECT_POST_PROCESSING_TEXT)
    else:
        await OrderState.WaitForAcceptance.set()
        await message.reply(
            general_text,
            reply_markup=acceptance_keyboard
        )


@dp.callback_query_handler(text="accept", state=OrderState.WaitForAcceptance)
async def send_order(call: types.CallbackQuery, state: FSMContext):
    try:
        async with state.proxy() as data:
            id = data.get('order_id')
            data.pop('order_id', 'default')
            db.save_orders_info(id, data)
    except Exception:
        pass
    finally:
        await state.finish()


@dp.callback_query_handler(text="decline", state=OrderState.WaitForAcceptance)
async def cancel_order(call: types.CallbackQuery, state: FSMContext):
    await call.answer('Вы отменили заказ', show_alert=True)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(
        make_order,
        state='*'
    )
    dp.register_message_handler(
        get_description,
        state=OrderState.WaitForDescription
    )
    dp.register_message_handler(
        get_sample,
        content_types=ContentType.PHOTO,
        state=OrderState.WaitForSample
    )
    dp.register_message_handler(
        get_quantity,
        state=OrderState.WaitForQuantity
    )
    dp.register_message_handler(
        get_length,
        state=OrderState.WaitForLength
    )
    dp.register_message_handler(
        get_width,
        state=OrderState.WaitForWidth
    )
    dp.register_message_handler(
        get_height,
        state=OrderState.WaitForHeight
    )
    dp.register_message_handler(
        get_material,
        state=OrderState.WaitForMaterial
    )
    dp.register_message_handler(
        get_color,
        state=OrderState.WaitForColor
    )
    dp.register_message_handler(
        send_order,
        state=OrderState.WaitForPostProcessing
    )
    dp.register_message_handler(
        get_post_processing,
        state=OrderState.WaitForAcceptance
    )
