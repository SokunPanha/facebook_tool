from flet import *
from api.profile import Profile
from flet_route import Basket, Params
class ProfileDataTable_ChBox(UserControl):
    def __init__(self,page:Page, params:Params, basket:Basket, route):
        super().__init__()
        self.profile = Profile()
        self.data = self.profile.find_all()
        self.page =page
        self.params =params 
        self.basket = basket
        self.route = route
        self.row = []
    def Delete(self,e):
            pname = e.control.data
            self.profile.delete(pname)
            self.page.update()
    def edit(self,  e):
        self.basket.data =e.control.data
        print(self.basket.data)
        self.page.update()
        self.page.go(self.route)
    def seleted_row(self,e):
         if e.control.value == True:
            self.row.append(e.control.data)
            print(self.row)
         else:
            self.row.pop(e.control.data[0])   
         print(e.control.data)
    def build(self):
        # page.update()

        data_table = DataTable(
                   show_checkbox_column= True,
                   width=900,
                   bgcolor= colors.GREY_900,
                   divider_thickness=0,
                   
                #    column_spacing=200,
                  columns=[
                       DataColumn(Text("Selected"),),DataColumn(Text("Profile Name")),DataColumn(Text("Email")), DataColumn(Text("Action", text_align= alignment.center)),]
            )
    
        for pname, user_data in self.data.items():
            data_table.rows.append(
                DataRow(  
                    cells=[
                        DataCell(
                             Checkbox(
                                  value = [pname],
                                      on_change= self.seleted_row
                                     ),
                                                           
                        ),
                        DataCell(Text(pname)),
                        DataCell(Text(user_data["email"])),
                        DataCell(Row(controls=[IconButton("EDIT", on_click= self.edit, data = [pname, user_data]) ,IconButton(icon=icons.DELETE, on_click= self.Delete, data= pname)]))
                    ],
                    
                )
            )    

        return data_table
           