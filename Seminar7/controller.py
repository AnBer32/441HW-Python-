import model
import view


def start():
    user_choice = 0
    while user_choice != 8:
        user_choice = view.main_menu()

        match user_choice:
            case 1:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book)
            case 2:
                model.open_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book()
                view.save_success()
            case 4:
                new = list(view.new_contact())
                model.update_phone_book(new)
                view.new_contact_success()
            case 5:
                contact_old = view.change_contact()
                result = model.search_contact(contact_old)
                view.show_contacts(result)
                if result:
                    contact_new = list(view.new_contact())
                    model.change_contact(result, contact_new)
                view.change_contact_success()
            case 6:
                contact = view.del_contact()
                result = model.search_contact(contact)
                view.show_contacts(result)
                if result:
                    model.delete_contact(result)
                view.del_contact_success()
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result)