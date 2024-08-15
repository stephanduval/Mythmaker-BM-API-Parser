import sqlite3
import json
import os  # Ensure os is imported to use os.listdir and other OS-related functions


def create_database_and_tables(db_name):
    # Connect to the SQLite database
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    
    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS LocalUser (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        Id TEXT,
        UserName TEXT,
        Email TEXT,
        IconFileName TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Card (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        Card_Name TEXT,
        Card_Class TEXT,
        Card_Text TEXT,
        Card_Power INTEGER,
        Creature_attack INTEGER,
        Creature_defense INTEGER,
        Instant_level_delta INTEGER,
        Instant_XP_delta INTEGER,
        Instant_AttackModifier_delta INTEGER,
        Instant_ArmorClass_delta INTEGER,
        Instant_Perception_delta INTEGER,
        Instant_Intelligence_delta INTEGER,
        Instant_Wisdom_delta INTEGER,
        Instant_Charisma_delta INTEGER,
        Instant_Constitution_delta INTEGER,
        Instant_Dexterity_delta INTEGER,
        Instant_Strength_delta INTEGER,
        Instant_Health_delta INTEGER,
        Item_level_delta INTEGER,
        Item_XP_delta INTEGER,
        Item_AttackModifier_delta INTEGER,
        Item_ArmorClass_delta INTEGER,
        Item_Perception_delta INTEGER,
        Item_Intelligence_delta INTEGER,
        Item_Wisdom_delta INTEGER,
        Item_Charisma_delta INTEGER,
        Item_Constitution_delta INTEGER,
        Item_Dexterity_delta INTEGER,
        Item_Strength_delta INTEGER,
        Item_Health_delta INTEGER,
        Spell_level_delta INTEGER,
        Spell_XP_delta INTEGER,
        Spell_AttackModifier_delta INTEGER,
        Spell_ArmorClass_delta INTEGER,
        Spell_Perception_delta INTEGER,
        Spell_Intelligence_delta INTEGER,
        Spell_Wisdom_delta INTEGER,
        Spell_Charisma_delta INTEGER,
        Spell_Constitution_delta INTEGER,
        Spell_Dexterity_delta INTEGER,
        Spell_Strength_delta INTEGER,
        Spell_Health_delta INTEGER,
        Quest_level_delta INTEGER,
        Quest_XP_delta INTEGER,
        Quest_AttackModifier_delta INTEGER,
        Quest_ArmorClass_delta INTEGER,
        Quest_Perception_delta INTEGER,
        Quest_Intelligence_delta INTEGER,
        Quest_Wisdom_delta INTEGER,
        Quest_Charisma_delta INTEGER,
        Quest_Constitution_delta INTEGER,
        Quest_Dexterity_delta INTEGER,
        Quest_Strength_delta INTEGER,
        Quest_Health_delta INTEGER,
        QuestionText TEXT,
        YesTrait TEXT,
        YesTraitDelta INTEGER,
        NoTrait TEXT,
        NoTraitDelta INTEGER,
        Value INTEGER,
        Image_FileName TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS LocalCharacter (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        CharacterName TEXT,
        Heritage TEXT,
        Class TEXT,
        Level INTEGER,
        XP INTEGER,
        AttackModifier INTEGER,
        ArmorClass INTEGER,
        Perception INTEGER,
        Intelligence INTEGER,
        Wisdom INTEGER,
        Charisma INTEGER,
        Constitution INTEGER,
        Dexterity INTEGER,
        Strength INTEGER,
        Health INTEGER
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Inventory (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        ItemName TEXT,
        Description TEXT,
        Category TEXT,
        Rarity TEXT,
        Value INTEGER,
        Image_FileName TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Quest (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT,
        LongTextBlock TEXT,
        Reward TEXT,
        PictureFileName TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Place (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        GPSCoordinates TEXT,
        AddedBy TEXT,
        Info TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Message (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Time TEXT,
        Sender TEXT,
        GPSCoordinate TEXT,
        MessageContent TEXT,
        Item TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PlayerClass (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        Class_Name TEXT,
        Description TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Player_Heritage (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        Heritage_Name TEXT,
        Description TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CurrentCharacterStats (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        CharacterName TEXT,
        Heritage TEXT,
        Class TEXT,
        Level INTEGER,
        XP INTEGER,
        AttackModifier INTEGER,
        ArmorClass INTEGER,
        Perception INTEGER,
        Intelligence INTEGER,
        Wisdom INTEGER,
        Charisma INTEGER,
        Constitution INTEGER,
        Dexterity INTEGER,
        Strength INTEGER,
        Health INTEGER
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS BurnEvent (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        event_id INTEGER,
        title TEXT,
        uid TEXT,
        description TEXT,
        event_type_id INTEGER,
        year INTEGER,
        print_description TEXT,
        slug TEXT,
        hosted_by_camp TEXT,
        located_at_art TEXT,
        other_location TEXT,
        check_location INTEGER,
        url TEXT,
        all_day TEXT,
        contact TEXT,
        FOREIGN KEY(event_type_id) REFERENCES BurnEventType(AutoId)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS BurnEventType (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        label TEXT,
        abbr TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS BurnEventOccurrenceSet (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        BurnEventId INTEGER,
        start_time TEXT,
        end_time TEXT,
        FOREIGN KEY(BurnEventId) REFERENCES BurnEvent(AutoId)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Art (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        Uid TEXT,
        Year INTEGER,
        Name TEXT,
        Url TEXT,
        ContactEmail TEXT,
        Hometown TEXT,
        Description TEXT,
        Artist TEXT,
        Category TEXT,
        Program TEXT,
        DonationLink TEXT,
        GuidedTours INTEGER,
        SelfGuidedTourMap INTEGER,
        LocationString TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ArtLocation (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        ArtId INTEGER,
        LocationString TEXT,
        Hour INTEGER,
        Minute INTEGER,
        Distance INTEGER,
        LocationCategory TEXT,
        GpsLatitude REAL,
        GpsLongitude REAL,
        FOREIGN KEY(ArtId) REFERENCES Art(AutoId)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ArtImage (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        ArtId INTEGER,
        GalleryRef TEXT,
        ThumbnailUrl TEXT,
        FOREIGN KEY(ArtId) REFERENCES Art(AutoId)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Camp (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        uid TEXT,
        year INTEGER,
        name TEXT,
        url TEXT,
        contact_email TEXT,
        hometown TEXT,
        description TEXT,
        landmark TEXT,
        location_string TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CampLocation (
        AutoId INTEGER PRIMARY KEY AUTOINCREMENT,
        CampId INTEGER,
        string TEXT,
        frontage TEXT,
        intersection TEXT,
        intersection_type TEXT,
        dimensions TEXT,
        exact_location TEXT,
        FOREIGN KEY(CampId) REFERENCES Camp(AutoId)
    )
    ''')

    return connection, cursor


# Insert or get BurnEventType
def get_or_create_event_type(cursor, event_type_data):
    if event_type_data:
        cursor.execute('''
            SELECT AutoId FROM BurnEventType WHERE label = ? AND abbr = ?
        ''', (event_type_data['label'], event_type_data['abbr']))
        
        result = cursor.fetchone()
        
        if result:
            return result[0]
        else:
            cursor.execute('''
                INSERT INTO BurnEventType (label, abbr)
                VALUES (?, ?)
            ''', (event_type_data['label'], event_type_data['abbr']))
            return cursor.lastrowid
    else:
        return None

# Insert BurnEvent and related occurrences
def insert_burn_event(cursor, event_data):
    event_type_id = get_or_create_event_type(cursor, event_data.get('event_type'))

    cursor.execute('''
        INSERT INTO BurnEvent (
            event_id, title, uid, description, event_type_id, year, print_description, slug, 
            hosted_by_camp, located_at_art, other_location, check_location, url, all_day, contact
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        event_data.get('event_id'),
        event_data.get('title'),
        event_data.get('uid'),
        event_data.get('description'),
        event_type_id,
        event_data.get('year'),
        event_data.get('print_description') if event_data.get('print_description') else None,
        event_data.get('slug'),
        event_data.get('hosted_by_camp'),
        event_data.get('located_at_art'),
        event_data.get('other_location'),
        event_data.get('check_location'),
        event_data.get('url'),
        event_data.get('all_day'),
        event_data.get('contact')
    ))

    burn_event_id = cursor.lastrowid

    for occurrence in event_data.get('occurrence_set', []):
        cursor.execute('''
            INSERT INTO BurnEventOccurrenceSet (
                BurnEventId, start_time, end_time
            ) VALUES (?, ?, ?)
        ''', (
            burn_event_id,
            occurrence.get('start_time'),
            occurrence.get('end_time')
        ))

def load_data_from_json(cursor, json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            events = json.load(file)
            for event in events:
                insert_burn_event(cursor, event)
    except FileNotFoundError:
        print(f"File {json_file_path} not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

# Insert Camp and related CampLocation
def insert_camp(cursor, camp_data):
    # Insert into the Camp table
    cursor.execute('''
        INSERT INTO Camp (
            uid, year, name, url, contact_email, hometown, description, landmark, location_string
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        camp_data.get('uid'),
        camp_data.get('year'),
        camp_data.get('name'),
        camp_data.get('url'),
        camp_data.get('contact_email'),
        camp_data.get('hometown'),
        camp_data.get('description'),
        camp_data.get('landmark'),
        camp_data.get('location_string')
    ))

    camp_id = cursor.lastrowid

    # Insert into the CampLocation table if location data exists
    location_data = camp_data.get('location')
    if location_data:
        cursor.execute('''
            INSERT INTO CampLocation (
                CampId, string, frontage, intersection, intersection_type, dimensions, exact_location
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            camp_id,
            location_data.get('string'),
            location_data.get('frontage'),
            location_data.get('intersection'),
            location_data.get('intersection_type'),
            location_data.get('dimensions'),
            location_data.get('exact_location')
        ))

def load_camp_data_from_json(cursor, json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            camps = json.load(file)
            for camp in camps:
                insert_camp(cursor, camp)
    except FileNotFoundError:
        print(f"File {json_file_path} not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

# Insert Art and related ArtLocation and ArtImage
def insert_art(cursor, art_data):
    # Insert into the Art table
    cursor.execute('''
        INSERT INTO Art (
            Uid, Year, Name, Url, ContactEmail, Hometown, Description, 
            Artist, Category, Program, DonationLink, GuidedTours, 
            SelfGuidedTourMap, LocationString
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        art_data.get('uid'),
        art_data.get('year'),
        art_data.get('name'),
        art_data.get('url'),
        art_data.get('contact_email'),
        art_data.get('hometown'),
        art_data.get('description'),
        art_data.get('artist'),
        art_data.get('category'),
        art_data.get('program'),
        art_data.get('donation_link'),
        art_data.get('guided_tours'),
        art_data.get('self_guided_tour_map'),
        art_data.get('location_string')
    ))

    art_id = cursor.lastrowid

    # Insert into the ArtLocation table if location data exists
    location_data = art_data.get('location')
    if location_data:
        cursor.execute('''
            INSERT INTO ArtLocation (
                ArtId, LocationString, Hour, Minute, Distance, LocationCategory, 
                GpsLatitude, GpsLongitude
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            art_id,
            location_data.get('string'),
            location_data.get('hour'),
            location_data.get('minute'),
            location_data.get('distance'),
            location_data.get('category'),
            location_data.get('gps_latitude'),
            location_data.get('gps_longitude')
        ))

    # Insert into the ArtImage table if images data exists
    images_data = art_data.get('images')
    if images_data:
        for image in images_data:
            cursor.execute('''
                INSERT INTO ArtImage (
                    ArtId, GalleryRef, ThumbnailUrl
                ) VALUES (?, ?, ?)
            ''', (
                art_id,
                image.get('gallery_ref'),
                image.get('thumbnail_url')
            ))

def load_art_data_from_json(cursor, json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            art_pieces = json.load(file)
            for art in art_pieces:
                insert_art(cursor, art)
    except FileNotFoundError:
        print(f"File {json_file_path} not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

def insert_initial_data(cursor):
    # Data for PlayerClass table
    player_classes = [
        {"Class_Name": "Artificer", "Description": "Master craftsmen and inventors - create magical items - devices - and fortifications."},
        {"Class_Name": "Bard", "Description": "Viking poets and musicians - weave magic through music - inspire allies - and influence with tales."},
        {"Class_Name": "Berserker", "Description": "Odin's chosen warriors for Ragnarok - fierce fighters skilled with axe and shield. Possess immense strength - courage - and frenzied battle prowess."},
        {"Class_Name": "Cleric", "Description": "Viking spiritual leaders with divine magic - heal - defend - and inspire through communion with gods."},
        {"Class_Name": "Druid", "Description": "Nature-connected seeresses - shapeshift - summon elementals - and command animals using mystical powers."},
        {"Class_Name": "Monk", "Description": "Spiritual martial artists - agile and powerful - resist mental attacks - strike precisely in combat."},
        {"Class_Name": "Paladin", "Description": "Noble warriors infused with divine magic - champions of gods - protect - heal - and inspire allies."},
        {"Class_Name": "Ranger", "Description": "Viking hunters and survivalists - adept with bow and spear - excel in wilderness tracking and combat."},
        {"Class_Name": "Rogue", "Description": "Viking scouts and stealth experts - navigate wilds - set traps - and ambush foes with stealth attacks."},
        {"Class_Name": "Sorcerer", "Description": "Raw magic wielders - tap primal power - cast unique spells - and enhance casting abilities."},
        {"Class_Name": "Warlock", "Description": "Pact-bound magic users - invoke patron's power - summon creatures - and manipulate with forbidden knowledge."},
        {"Class_Name": "Wizard", "Description": "Learned rune wielders mastering magic - cast spells using runic inscriptions - manipulate nature and illusions."}
    ]

    # Insert PlayerClass data
    for player_class in player_classes:
        cursor.execute('''
            INSERT INTO PlayerClass (Class_Name, Description)
            VALUES (?, ?)
        ''', (player_class['Class_Name'], player_class['Description']))

    # Data for Player_Heritage table
    player_heritages = [
        {"Heritage_Name": "Aasimar", "Description": "Blessed by the gods - seen as descendants of the Aesir - the main pantheon of gods in Norse mythology."},
        {"Heritage_Name": "Dark Elf", "Description": "Elves who live underground and are known for their dark magic. They are often in conflict with the Ljósálfar."},
        {"Heritage_Name": "Dragonborn", "Description": "Inspired by the dragons of Norse mythology - they are powerful and feared warriors."},
        {"Heritage_Name": "Dwarf", "Description": "Known for their craftsmanship and resilience - Dwarves in Norse mythology are often skilled blacksmiths and miners."},
        {"Heritage_Name": "Elf", "Description": "Ethereal beings deeply connected with magic. They are often seen as aloof by other heritages."},
        {"Heritage_Name": "Gnome", "Description": "Small - often invisible beings known for their mischief - cunning - and magical abilities."},
        {"Heritage_Name": "Half-Elf", "Description": "The product of the union between humans and elves - they combine the adaptability of humans with the mystical affinity of the elves."},
        {"Heritage_Name": "Half-Jötunn", "Description": "The offspring of a human and a jǫtunn (giant) - they combine the strength of the giants with the adaptability of humans."},
        {"Heritage_Name": "Halfling", "Description": "Humans of small stature known for their luck - agility - and charm."},
        {"Heritage_Name": "Human", "Description": "The most adaptable and diverse heritage. Humans in a Viking-themed campaign are likely to be the majority - leading lives as farmers - sailors - warriors - and skalds."},
        {"Heritage_Name": "Jötunn", "Description": "The giants of Norse mythology - known for their immense size and strength."},
        {"Heritage_Name": "Tiefling", "Description": "Descendants of beings from the underworld - marked by Hel - the Norse goddess of death."}
    ]

    # Insert Player_Heritage data
    for heritage in player_heritages:
        cursor.execute('''
            INSERT INTO Player_Heritage (Heritage_Name, Description)
            VALUES (?, ?)
        ''', (heritage['Heritage_Name'], heritage['Description']))


field_acronyms = {
    "Card_Name": "CRD",
    "Card_Class": "CLS",
    "Card_Text": "TXT",
    "Card_Power": "PWR",
    "Creature_attack": "ATK",
    "Creature_defense": "DEF",
    "Instant_level_delta": "ILD",
    "Instant_XP_delta": "IXP",
    "Instant_AttackModifier_delta": "ISAM",
    "Instant_ArmorClass_delta": "ISAC",
    "Instant_Perception_delta": "ISPR",
    "Instant_Intelligence_delta": "ISIN",
    "Instant_Wisdom_delta": "ISWS",
    "Instant_Charisma_delta": "ISCH",
    "Instant_Constitution_delta": "ISCO",
    "Instant_Dexterity_delta": "ISDX",
    "Instant_Strength_delta": "ISST",
    "Instant_Health_delta": "ISHL",
    "Item_level_delta": "ILD",
    "Item_XP_delta": "IXP",
    "Item_AttackModifier_delta": "ITAM",
    "Item_ArmorClass_delta": "ITAC",
    "Item_Perception_delta": "ITR",
    "Item_Intelligence_delta": "ITIN",
    "Item_Wisdom_delta": "ITWS",
    "Item_Charisma_delta": "ITCH",
    "Item_Constitution_delta": "ITCO",
    "Item_Dexterity_delta": "ITDX",
    "Item_Strength_delta": "ITST",
    "Item_Health_delta": "ITHL",
    "Spell_level_delta": "SLD",
    "Spell_XP_delta": "SXP",
    "Spell_AttackModifier_delta": "SAM",
    "Spell_ArmorClass_delta": "SAC",
    "Spell_Perception_delta": "SPR",
    "Spell_Intelligence_delta": "SIN",
    "Spell_Wisdom_delta": "SWS",
    "Spell_Charisma_delta": "SCH",
    "Spell_Constitution_delta": "SCO",
    "Spell_Dexterity_delta": "SDX",
    "Spell_Strength_delta": "SST",
    "Spell_Health_delta": "SHL",
    "Quest_level_delta": "QLD",
    "Quest_XP_delta": "QXP",
    "Quest_AttackModifier_delta": "QAM",
    "Quest_ArmorClass_delta": "QAC",
    "Quest_Perception_delta": "QPR",
    "Quest_Intelligence_delta": "QIN",
    "Quest_Wisdom_delta": "QWS",
    "Quest_Charisma_delta": "QCH",
    "Quest_Constitution_delta": "QCO",
    "Quest_Dexterity_delta": "QDX",
    "Quest_Strength_delta": "QST",
    "Quest_Health_delta": "QHL",
    "QuestionText": "QST",
    "YesTrait": "YTR",
    "YesTraitDelta": "YTD",
    "NoTrait": "NTR",
    "NoTraitDelta": "NTD",
    "Value": "VAL",
    "Image_FileName": "IMG"
}


def insert_card(cursor, card_data):
    cursor.execute('''
        INSERT INTO Card (
            Card_Name, Card_Class, Card_Text, Card_Power, Creature_attack, Creature_defense,
            Instant_level_delta, Instant_XP_delta, Instant_AttackModifier_delta, Instant_ArmorClass_delta,
            Instant_Perception_delta, Instant_Intelligence_delta, Instant_Wisdom_delta, Instant_Charisma_delta,
            Instant_Constitution_delta, Instant_Dexterity_delta, Instant_Strength_delta, Instant_Health_delta,
            Item_level_delta, Item_XP_delta, Item_AttackModifier_delta, Item_ArmorClass_delta,
            Item_Perception_delta, Item_Intelligence_delta, Item_Wisdom_delta, Item_Charisma_delta,
            Item_Constitution_delta, Item_Dexterity_delta, Item_Strength_delta, Item_Health_delta,
            Spell_level_delta, Spell_XP_delta, Spell_AttackModifier_delta, Spell_ArmorClass_delta,
            Spell_Perception_delta, Spell_Intelligence_delta, Spell_Wisdom_delta, Spell_Charisma_delta,
            Spell_Constitution_delta, Spell_Dexterity_delta, Spell_Strength_delta, Spell_Health_delta,
            Quest_level_delta, Quest_XP_delta, Quest_AttackModifier_delta, Quest_ArmorClass_delta,
            Quest_Perception_delta, Quest_Intelligence_delta, Quest_Wisdom_delta, Quest_Charisma_delta,
            Quest_Constitution_delta, Quest_Dexterity_delta, Quest_Strength_delta, Quest_Health_delta,
            QuestionText, YesTrait, YesTraitDelta, NoTrait, NoTraitDelta, Value, Image_FileName
        ) VALUES (
            :Card_Name, :Card_Class, :Card_Text, :Card_Power, :Creature_attack, :Creature_defense,
            :Instant_level_delta, :Instant_XP_delta, :Instant_AttackModifier_delta, :Instant_ArmorClass_delta,
            :Instant_Perception_delta, :Instant_Intelligence_delta, :Instant_Wisdom_delta, :Instant_Charisma_delta,
            :Instant_Constitution_delta, :Instant_Dexterity_delta, :Instant_Strength_delta, :Instant_Health_delta,
            :Item_level_delta, :Item_XP_delta, :Item_AttackModifier_delta, :Item_ArmorClass_delta,
            :Item_Perception_delta, :Item_Intelligence_delta, :Item_Wisdom_delta, :Item_Charisma_delta,
            :Item_Constitution_delta, :Item_Dexterity_delta, :Item_Strength_delta, :Item_Health_delta,
            :Spell_level_delta, :Spell_XP_delta, :Spell_AttackModifier_delta, :Spell_ArmorClass_delta,
            :Spell_Perception_delta, :Spell_Intelligence_delta, :Spell_Wisdom_delta, :Spell_Charisma_delta,
            :Spell_Constitution_delta, :Spell_Dexterity_delta, :Spell_Strength_delta, :Spell_Health_delta,
            :Quest_level_delta, :Quest_XP_delta, :Quest_AttackModifier_delta, :Quest_ArmorClass_delta,
            :Quest_Perception_delta, :Quest_Intelligence_delta, :Quest_Wisdom_delta, :Quest_Charisma_delta,
            :Quest_Constitution_delta, :Quest_Dexterity_delta, :Quest_Strength_delta, :Quest_Health_delta,
            :QuestionText, :YesTrait, :YesTraitDelta, :NoTrait, :NoTraitDelta, :Value, :Image_FileName
        )
    ''', card_data)

def process_files_and_add_cards(folder_path, cursor):
    for file_name in os.listdir(folder_path):
        if file_name.endswith((".jpg", ".jpeg", ".png")):
            parts = file_name.split("-")
            if len(parts) > 3 and parts[0] == "MM":
                card_name = parts[2].replace('_', ' ')
                card_data = {
                    "Card_Name": card_name,
                    "Card_Class": None,
                    "Card_Text": None,
                    "Card_Power": None,
                    "Creature_attack": None,
                    "Creature_defense": None,
                    "Instant_level_delta": None,
                    "Instant_XP_delta": None,
                    "Instant_AttackModifier_delta": None,
                    "Instant_ArmorClass_delta": None,
                    "Instant_Perception_delta": None,
                    "Instant_Intelligence_delta": None,
                    "Instant_Wisdom_delta": None,
                    "Instant_Charisma_delta": None,
                    "Instant_Constitution_delta": None,
                    "Instant_Dexterity_delta": None,
                    "Instant_Strength_delta": None,
                    "Instant_Health_delta": None,
                    "Item_level_delta": None,
                    "Item_XP_delta": None,
                    "Item_AttackModifier_delta": None,
                    "Item_ArmorClass_delta": None,
                    "Item_Perception_delta": None,
                    "Item_Intelligence_delta": None,
                    "Item_Wisdom_delta": None,
                    "Item_Charisma_delta": None,
                    "Item_Constitution_delta": None,
                    "Item_Dexterity_delta": None,
                    "Item_Strength_delta": None,
                    "Item_Health_delta": None,
                    "Spell_level_delta": None,
                    "Spell_XP_delta": None,
                    "Spell_AttackModifier_delta": None,
                    "Spell_ArmorClass_delta": None,
                    "Spell_Perception_delta": None,
                    "Spell_Intelligence_delta": None,
                    "Spell_Wisdom_delta": None,
                    "Spell_Charisma_delta": None,
                    "Spell_Constitution_delta": None,
                    "Spell_Dexterity_delta": None,
                    "Spell_Strength_delta": None,
                    "Spell_Health_delta": None,
                    "Quest_level_delta": None,
                    "Quest_XP_delta": None,
                    "Quest_AttackModifier_delta": None,
                    "Quest_ArmorClass_delta": None,
                    "Quest_Perception_delta": None,
                    "Quest_Intelligence_delta": None,
                    "Quest_Wisdom_delta": None,
                    "Quest_Charisma_delta": None,
                    "Quest_Constitution_delta": None,
                    "Quest_Dexterity_delta": None,
                    "Quest_Strength_delta": None,
                    "Quest_Health_delta": None,
                    "QuestionText": None,
                    "YesTrait": None,
                    "YesTraitDelta": None,
                    "NoTrait": None,
                    "NoTraitDelta": None,
                    "Value": None,
                    "Image_FileName": file_name
                }

                # Process the remaining parts for attributes and values until "END" is found
                for i in range(3, len(parts) - 1, 2):
                    if parts[i] == "END":
                        break  # Stop parsing if "END" is encountered

                    acronym = parts[i]
                    if i + 1 < len(parts):  # Ensure there's a value after the acronym
                        value = int(parts[i + 1]) if parts[i + 1].isdigit() else None
                        field_name = next((key for key, val in field_acronyms.items() if val == acronym), None)
                        if field_name:
                            card_data[field_name] = value

                insert_card(cursor, card_data)
                print(f"Added card: {card_name} from file {file_name}")


def main():
    db_name = 'myDatabase.db'
    connection, cursor = create_database_and_tables(db_name)

    # Load BurnEvents data
    load_data_from_json(cursor, 'API Data/2024_event.json')

    # Load Camp data
    load_camp_data_from_json(cursor, 'API Data/2024_camp.json')

    # Load Art data
    load_art_data_from_json(cursor, 'API Data/2024_art.json')

    # Insert initial data for PlayerClass and Player_Heritage
    insert_initial_data(cursor)


    folder_path = '/home/elcid/Documents/Unity Projects/The Mythmaker Quest/Assets/Images/XRImages/Cards'
    
    process_files_and_add_cards(folder_path, cursor)

    connection.commit()
    connection.close()

if __name__ == '__main__':
    main()