import os
from time import sleep
from tkinter import *
from tkinter import filedialog

win = Tk()
logo_p = []
dir_p = []


def get_logo(n):
    file = filedialog.askopenfile(initialdir='.', filetypes=(('PNG', '*.png'), ("All Files", "*.*")))
    try:
        path = str(file.name)
        s_name = path.split('/')
        name = s_name[len(s_name) - 1]
        TEXT = Label(win, text=name)
        TEXT.grid(row=4, column=1)
    except AttributeError:
        pass
    logo_p.append(file.name)


def get_dir(n):
    file = filedialog.askdirectory(initialdir='.')
    dir_p.append(file)
    path = str(file)
    s_name = path.split('/')
    name = s_name[len(s_name) - 1]
    try:
        TEXT = Label(win, text=name)
        TEXT.grid(row=6, column=1)
    except AttributeError:
        pass


def submit(mod_id_en, name_en):
    mod_id_bool = False
    mod_name_bool = False
    dir_path_bool = False
    logo_path_bool = False
    mod_id_uc = str(mod_id_en.get(1.0, END)).replace(" ", "_").lower().strip('\n,./?";:{}[]()_-+=')
    name_uc = str(name_en.get(1.0, END)).strip(' \n')
    print(mod_id_uc)
    print(name_uc)
    if mod_id_uc == '':
        print('Invalid Mod Id')
        mod_id_bool = False
        pass
    else:
        if name_uc.strip('\n ') == '':
            print('Invalid Mod Name')
            mod_name_bool = False
            pass


    return


def AddWidgets():
    HeadLabel = Label(win, text='Mod Organizer', font=('Aerial', 12))
    HeadLabel.grid(row=0, column=1, pady=10, padx=25)
    # ID
    MOD_ID_TEXT = Label(win, text='MOD ID:')
    MOD_ID_TEXT.grid(row=1, pady=10, column=0)
    MOD_ID_SPACE = Text(win, width=20, height=1)
    MOD_ID_SPACE.grid(row=1, pady=10, column=1)
    # NAME
    MOD_NAME_TEXT = Label(win, text='MOD NAME:')
    MOD_NAME_TEXT.grid(row=2, pady=10, column=0)
    MOD_NAME_SPACE = Text(win, width=20, height=1)
    MOD_NAME_SPACE.grid(row=2, pady=10, column=1)
    # LOGO
    LOGO_TEXT = Label(win, text='LOGO:')
    LOGO_TEXT.grid(row=3, pady=10, column=0)
    LOGO_BUTTON = Button(win, text='Open File', command=lambda: get_logo(n=1))
    LOGO_BUTTON.grid(row=3, pady=10, column=1)
    # MOD DIR
    MOD_DIR_TEXT = Label(win, text='MOD DIR:')
    MOD_DIR_TEXT.grid(row=5, pady=10, column=0)
    MOD_DIR_BUTTON = Button(win, text='Open Folder', command=lambda: get_dir(n=1))
    MOD_DIR_BUTTON.grid(row=5, pady=10, column=1)
    # SUBMIT
    SUBMIT = Button(win, text='Submit', command=lambda: submit(MOD_ID_SPACE, MOD_NAME_SPACE), width=20)
    SUBMIT.grid(row=7, column=1, pady=10)


def clearing_items(f_name, ID):
    try:
        os.chdir(f_name)
        os.remove('CREDITS.txt')
        os.remove('changelog.txt')
        os.remove('.gitattributes')
        os.remove('.gitignore')
    except FileNotFoundError:
        pass
        sleep(1)
    try:
        os.mkdir('textures')
    except FileExistsError:
        pass
    try:
        file = open('mod_id.txt', 'w+')
        file.write(ID)
        file.close()
    except:
        print("Failed To Adding MOD_ID")
    os.chdir('../')


def renaming_file(f_name, ID):
    try:
        os.chdir(f_name)
        os.chdir('src/main/java')
        try:
            os.mkdir('me')
        except FileExistsError:
            pass
        try:
            os.mkdir('me/eza')
        except FileExistsError:
            pass
        try:
            os.mkdir('me/eza/' + ID)
        except FileExistsError:
            pass
        file = open('me/eza/' + ID + "/Main.java", 'w+')
        file.write('package me.eza.' + ID + ';')
        file.write('''

@Mod(Main.ID)
public class Main {
''')
        file.write('public static final String ID = "' + ID + '";')
        file.write('''
    private static final Logger LOGGER = LogManager.getLogger();
    public ExampleMod() {
        MinecraftForge.EVENT_BUS.register(this);
    }
        ''')
    except:
        print("Error Found")
    file = open('me/eza/' + ID + '/UseFull.txt', 'w+')
    file.write('''
public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, Main.ID);
public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, Main.ID);

public static final RegistryObject<Item> TEST = ITEMS.register("test", () -> new BeefBurgers(new Item.Properties().tab(CreativeModeTab.TAB_MISC).rarity(Rarity.EPIC)));
    ''')
    os.chdir('../')


def toml_page(MOD_ID, MOD_NAME, LOGO):
    logo = ''
    if LOGO == '':
        logo = 'examplemod.png'
    else:
        logo = LOGO
    os.chdir('resources/META-INF')
    file = open('mods.toml', 'w+')
    file.write('''modLoader="javafml"
LoaderVersion="[37,)"
license="All rights reserved"
[[mods]]
''')
    file.write('modId="' + MOD_ID + '"\nversion="${file.jarVersion}"\n')
    file.write('displayName="' + MOD_NAME + '"\n')
    file.write('logoFile="' + logo + '"\n')
    file.write('credits="Thanks for Downloading Our New Mod"\n')
    file.write('authors="Eza"\n')
    file.write('description=""""""\n')
    file.write('''
# [[dependencies.examplemod]]   
#     modId="forge"
#     mandatory=true
#     versionRange="[37,)"
#     ordering="NONE"
#     side="BOTH"
# [[dependencies.examplemod]]
#     modId="minecraft"
#     mandatory=true
#     versionRange="[1.17.1,1.18)"
#     ordering="NONE"
#     side="BOTH"
    ''')
    win.destroy()


def work(ID, NAME, LOGO, DIR):
    clearing_items(DIR, ID)
    renaming_file(DIR, ID)
    toml_page(ID, NAME, LOGO)


def main():
    win.title('Mod Organizer')
    win.geometry('300x300')
    AddWidgets()
    win.mainloop()


if __name__ == '__main__':
    main()
