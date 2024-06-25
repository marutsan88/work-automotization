from address import Address
from mailing import Mailing

to_address = Address("347894", "Крыжопль", "Улица Больших затейников", "20", "15")
from_address = Address("654321", "Магадан", "Улица Свободы", "15", "18")
mailing = Mailing(to_address, from_address, 100, "DMA123")

print(f"Отправление {mailing.track} из {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house}:{to_address.apartment} "
      f"в {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house}:{from_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")

