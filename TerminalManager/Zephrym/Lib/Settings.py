""" Summary
#*    Handles the majority of your settings.
#*    300+ and counting possible settings.
TODO: initial release has pending fixes
TODO: Add in custom support for LineEdits and PushButtons
TODO: Add in a more user friendly implementation of radio buttons.
    FIXME: Review this class before initial release
        FIXME: Review this class before initial release. If you see this then you are on the pre-release version

"""
text = "[zLib]:"
import inspect

try:
    import Terminal
except ModuleNotFoundError:
    from Lib.Terminal import Terminal

class Settings:
    # TODO: Clean up long replace chains in assertions
    @staticmethod
    def __boolean_assert(name, boolean, s_0_3, s_1_2, s_1_4):
        try:
            assert type(boolean) is bool
            Terminal.SetCheckBox(name, boolean)
        except AssertionError or NameError or TypeError:
            exit(str(s_0_3) + "() has exited with error! See below for details on how to fix this.\n"
                 + "You used " + boolean + " as a "
                 + str(type(boolean)).replace("<", "").replace(">", "").replace("class", "").replace(" ", "").replace("'", "")
                 + " only use True or False as a "
                 + str(type(True)).replace("<", "").replace(">", "").replace("class", "").replace(" ", "").replace("'", "")
                 + ".\n" + "your implementation of Settings."
                 + str(s_0_3) + "() is incorrect. please inspect it on line ("
                 + str(s_1_2) + ")\nCheck your parameter's or arguments in this code context: "
                 + str(s_1_4).replace(" ", "").replace("'", "").replace("\\n", "") + " [" + boolean + "] is the most likely culprit")

    @staticmethod
    def __int_assert(name, integer, s_0_3, s_1_2, s_1_4):
        try:
            assert type(integer) is int
            Terminal.SetComboBox(name, integer)
        except AssertionError or NameError or TypeError:
            exit(str(s_0_3) + "() has exited with error! See below for details on how to fix this.\n"
                 + "You used " + integer + " as a "
                 + str(type(integer)).replace("<", "").replace(">", "").replace("class", "").replace(" ", "").replace("'", "")
                 + " only use a non decimal number as a "
                 + str(type(1)).replace("<", "").replace(">", "").replace("class", "").replace(" ", "").replace("'", "")
                 + ".\n" + "your implementation of Settings."
                 + str(s_0_3) + "() is incorrect. please inspect it on line ("
                 + str(s_1_2) + ")\nCheck your parameter's or arguments in this code context: "
                 + str(s_1_4).replace(" ", "").replace("'", "").replace("\\n", "") + " [" + integer + "] is the most likely culprit")

    @staticmethod
    def auto_ap(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto AP", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_attack(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto Attack", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_buff(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto Buff", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_die(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto Die", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_die_by_mob(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("bot/auto_die/bymob", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_equip(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto Equip", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def demonavenger_auto_exceed(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto Exceed", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_feed_pet(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto Feed", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_hp_pot(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto HP", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_login(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto Login", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_loot(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto Loot", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_mission(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto Mission", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_mp(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto MP", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_npc(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto NPC", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_pet(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto Pet", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_revive(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto Revive", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_rune(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto Rune", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_sp(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto SP", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def buy_arrows(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Buy Arrows", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def buy_hp_pot(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Buy HP Pot", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def buy_mp_pot(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Buy MP Pot", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def buy_pet_food(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Buy Pet Food", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def buy_return_scroll(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Buy Return Scroll", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def beasttamer_mode_check(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("beastTamerModeCheck", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def blaster_infinite_bullets(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Infinite Bullets", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def bowmaster_unlimited_arrow_platter(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Unlimtd Arrow Platter", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def mob_auto_aggro(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Auto Aggro", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def blazewizard_blazing_extinction_nodelay(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Delay Blazing Extinction", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def blazewizard_no_blazing_extinction(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Blazing Extinction Effect", boolean, traceback[0], traceback[1],
                                  traceback[2])

    @staticmethod
    def blazewizard_flame_orb_hack(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Flame Orb Hack", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def spawn_point_control_current_location(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Current location", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def no_background(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Background", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def no_blue_boxes(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Blue Boxes", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def no_boss_map_effect(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Boss Map Effect", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def no_damage_info(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Damage Info", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def no_fade_animation(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Fade Animation", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def no_fade_stages(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Fade Stages", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def no_loot_animation(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Loot Animation", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def no_map_object(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Map Object", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def no_skill_effect(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Skill Effect", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def no_tile_or_platform(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Tile", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def no_weather_effect(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Weather", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def remove_screen_clutter(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Remove Screen Clutter", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def disable_maple_guide(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Do not open Maple Guide on enter game", boolean, traceback[0], traceback[1],
                                  traceback[2])

    @staticmethod
    def disable_mileage_ui(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Do not open Mileage on enter game", boolean, traceback[0], traceback[1],
                                  traceback[2])

    @staticmethod
    def darkknight_la_mancha_spear_hack(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("La Mancha Spear Hack", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def drop_item_at_max_per_slot(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Drop item at max per slot", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def summon_familiar_0(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Familiar 0", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def summon_familiar_1(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Familiar 1", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def summon_familiar_2(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Familiar 2", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def full_map_attack(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Full Map Attack", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def general_fma(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("General FMA", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def godmode_30(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("30 Sec God Mode", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def godmode_full(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Full God Mode", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def godmode_guard(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Guard God Mode", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kami_ignore_elite_monster(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Ignore Elite Monster", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def ignore_skill_cooldown(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Ignore Skill Cooldown", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def instant_enchantment_scroll(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Instant Enchantment Scroll", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def instant_enchantment_star(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Instant Enchantment Star", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def instant_extraction(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Instant Extraction", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kinesis_instant_final_smash(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Instant Final Smash", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def jump_down_anywhere(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Jump Down Anywhere", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kami_to_mobs(boolean):  # same as kami_vac(). This is here for me because I think this name makes more sense.
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Kami Vac", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kami_vac(
            boolean):  # same as kami_to_mobs(). This is here for people who are looking through this based on what the ui says.
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Kami Vac", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kami_loot(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Kami Loot", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kami_grenade(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Grenade Kami", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kami_collision_items(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Kami Collision Items", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kami_no_air_check(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Air Check", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kanna_monkey_spirit_nodelay(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("MonkeySpiritsNDcheck", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def logo_skipper(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Logo Skipper", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def melee_no_delay(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Melee No Delay", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def mob_vac(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Mob Vac", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def mob_falldown(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Mob Falldown", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def mob_disarm(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Mob Disarm", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def mob_speed_up(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Mob Speed Up", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def mob_no_spawn_animation(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Mob No Spawn Animation", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def mob_no_death_animation(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Mob No Death Animation", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def sell_rush_equip(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("EQUIP Rush", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def sell_rush_etc(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("ETC Rush", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def buy_rush_mp(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("MP Pot Rush", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def slide_and_attack(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Slide And Attack", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def skill_injection(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Skill Injection", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def sell_potions(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Sell hp/mp pots", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def sell_filtered_items(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Sell filter item", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def rush_by_level(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Rush By Level", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def respond_gm(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Respond to GM ", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def portal_teleport_with_backspace(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Portal Teleport [Back Space]", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def pet_item_teleport(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Pet Item Teleport", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def offline_mode_enabled(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Offline Mode", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def npc_teleport_with_tab(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Npc Teleport [Tab]", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def no_rush_on_skill(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Rush", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def no_login_error(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Login Error", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def no_letter_box(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Letter Box", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def no_knock_back(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Knock Back", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def flash_jump_nodelay(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("No Delay Flash Jump", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def unlimited_attack(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Unlimtd Attack", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def unlimited_vitality_familiar(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Unlimited Vitality", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def sell_rush_use(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("USE Rush", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def blazewizard_throw_blazing_extinction(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Throw Blazing Extinction", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kanna_auto_kishin(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Summon Kishin", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def spawn_point_control(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Spawn Control", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def boss_vellum_freeze(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("Vellum Freeze", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def illium_radiant_javelin_nodelay(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("bot/illium/radiant_javelin_delay", boolean, traceback[0], traceback[1],
                                  traceback[2])

    @staticmethod
    def illium_summon_control(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("bot/illium/summon_control", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kanna_kami_ether_pulse(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("bot/kanna_kami", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kanna_kishin_fma(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("bot/kishin_fma", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def mercedes_hack(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("bot/mercedes_hack", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kami_portalkami(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("bot/portal_kami", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_obtain_puffram(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("bot/puffram", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def skill_injection_no_wait(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("bot/si_no_wait", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kami_summon(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("bot/summon_kami", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def transfer_item(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("bot/transfer/item", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def keep_meso(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("bot/transfer/keep_meso", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def transfer_meso(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("bot/transfer/meso", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kanna_charm_fma(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("charm_fma", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kami_dragon(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("dragon_kami", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def elite_cc(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("eliteCC", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def item_filter_all(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("filter_all", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def item_filter_card(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("filter_card", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def item_filter_equip(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("filter_equip", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def item_filter_etc(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("filter_etc", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def item_filter_familiar(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("filter_familiar", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def item_filter_recipe(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("filter_recipe", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def item_filter_setup(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("filter_setup", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def item_filter_use(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("filter_use", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def face_left(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("flacc", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def macro1(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("macro1_check", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def macro2(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("macro2_check", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def macro3(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("macro3_check", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def macro4(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("macro4_check", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def macro5(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("macro5_check", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def boss_freeze(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("main/boss_freeze", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def disable_quest_checks(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("main/disable_quest_checks", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def filter_elite(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("main/filter_elite_monster", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def memory_hack(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("main/memory_reducer", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def mob_no_jump(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("main/mobnojump", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def disable_all_quests(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("main/nolag", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def rush_with_hyper_rock(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("map/maprusher/hypertelerock", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def mob_vac_limit(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("mobvac_limit_check", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def jr_boogie_regen_nodelay(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("ndmp", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def node(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("node_check", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def reset_inner(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("reset_inner", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def scanner_show_tooltip(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("scanner/show_tooltip", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_burning_on_creation(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("settings/autoburn", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_character_creation(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("settings/autochar", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def block_quest_helper(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("settings/block_quest_helper", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def disable_joypad_detection(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("settings/disable_joypad_detection", boolean, traceback[0], traceback[1],
                                  traceback[2])

    @staticmethod
    def crash_exp(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("settings/expcrash", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def logout_exp(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("settings/explogout", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def login_wait(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("settings/loginwait", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def crash_meso(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("settings/mesocrash", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def logout_meso(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("settings/mesologout", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def traveling_merchant(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("settings/traveling_merchant", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def nebulite_fusion(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("special/neb", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def timed_cc(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("timedCCCheck", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def buy_rush_hp(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("HP Pot Rush", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def save_profile():
        Terminal.SaveProfile()

    @staticmethod
    def load_profile(path):
        Terminal.LoadProfile(path)

    @staticmethod
    def logout():
        Terminal.LogOut()

    @staticmethod
    def auto_cube(id, slot, grade = 4):
        Terminal.AutoCube(id, slot, grade)

    @staticmethod
    def skill_inject_id(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("SISkillID", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def attack_key(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("AttackKey", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def familiar_0_id(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("Familiar0", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def familiar_1_id(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("Familiar1", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def familiar_2_id(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("Familiar2", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def hp_key(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("HPKey", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def fixme_hacking_opt(integer):  # FIXME: Verify what this does
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("HackingOpt", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def login_channel_id(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("LoginChannel", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def login_server_id(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("LoginServer", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def login_world_id(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("LoginWorld", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def mp_key(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("MPKey", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def beasttamer_combo(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("beastTamerModeCombo", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def transfer_channel_id(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("bot/transfer/channelid", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def fixme_eva_cmb(integer):  # FIXME: Verify what this does
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("eva_cmb", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def macro1_combo(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("macro1_combo", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def macro2_combo(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("macro2_combo", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def macro3_combo(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("macro3_combo", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def macro4_combo(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("macro4_combo", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def macro5_combo(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("macro5_combo", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def set_resolution(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("resolution", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_char_job(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("settings/autochar_job", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def buy_arrow_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("Arrow", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_die_exp_percent(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("AutoDieExp", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_die_level(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("AutoDieLevel", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def filter_meso_above(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("FilterMeso", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def blazewizard_flame_ball_delay(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("FlameBall", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def gm_whisper_reset_time(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("GMWhisper", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def fixme_buy_hp_pot_amount(integer):  # FIXME: Verify what this does
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("HPPot", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kami_loot_item_threshold(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("KamiLoot", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def fixme_buy_mp_pot_amount(integer):  # FIXME: Verify what this does
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("MPPot", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kanna_monkey_spirit_nodelay_speed(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("MonkeySpiritsNDdelay", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def buy_pet_food_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("PetFood", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def fixme_skill_inject_delay(integer):  # FIXME: Verify what this does
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("SkillInjection", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_attack_delay(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("autoattack_spin", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_loot_delay(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("autoloot_spin", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def ball_count(integer):  # FIXME: Find out what this does
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("bot/ballcount", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def illium_radiant_javelin_delay(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("bot/illium/radiant_javelin", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kami_delay(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("bot/kami_delay", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kanna_kami_delay(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("bot/kanna_kami_delay", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def item_transfer_threshold(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("bot/transfer/item_threshold", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def meso_transfer_keep_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("bot/transfer/keep_meso", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def meso_transfer_threshold(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("bot/transfer/meso_threshold", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def kanna_charm_nodelay_speed(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("charm_delay", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def inner_pot_delay(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("inner_delay", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def macro1_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("macro1_spin", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def macro2_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("macro2_spin", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def macro3_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("macro3_spin", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def macro4_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("macro4_spin", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def macro5_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("macro5_spin", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def node_delay_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("node_delay", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def crash_exp_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("settings/expcrash", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def logout_exp_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("settings/explogout", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def login_wait_time(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("settings/loginwait1", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def login_wait_after_x_crash(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("settings/loginwait2", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def login_monitor_crash_timeout(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("settings/loginwait3", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def crash_meso_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("settings/mesocrash", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def logout_meso_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("settings/mesologout", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def buy_cubes_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("special/buy_cubes", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def timed_cc_delay(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("timedCCSpin", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_hp_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("sliderHP", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def auto_mp_amount(integer):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__int_assert("sliderMP", integer, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def mob_vac_radio_char(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        if boolean:
            Settings.__boolean_assert("MobVacChar", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def mob_vac_radio_specific(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        if boolean: Settings.__boolean_assert("MobVacChar", not boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def mob_vac_radio_pos_normal(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        if boolean: Settings.__boolean_assert("MobVacPos", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def mob_vac_radio_pos_airhit(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("MobVacPos", not boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def skill_inject_dragon(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        if boolean: Settings.__boolean_assert("SIRadioDragon", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def skill_inject_magic(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        if boolean: Settings.__boolean_assert("SIRadioMagic", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def skill_inject_melee(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        if boolean: Settings.__boolean_assert("SIRadioMelee", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def skill_inject_shoot(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        if boolean: Settings.__boolean_assert("SIRadioShoot", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def skill_inject_use_dropdown(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        if boolean: Settings.__boolean_assert("SkillInjection1", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def skill_inject_use_id(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        if boolean: Settings.__boolean_assert("SkillInjection2", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def fixme_mob_vac_new(boolean):  # FIXME: no clue what this does
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("bot/mobvac/new", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def fixme_mob_vac_old(boolean):  # FIXME: no clue what this does
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        Settings.__boolean_assert("bot/mobvac/old", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def skill_inject_cadena(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        if boolean: Settings.__boolean_assert("bot/si_cadena", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def buy_black_cube(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        if boolean: Settings.__boolean_assert("special/buy_cube_black", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def buy_red_cube(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        if boolean: Settings.__boolean_assert("special/buy_cube_red", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def inner_reset_until_legendary(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        if boolean: Settings.__boolean_assert("special/inner_legendary", boolean, traceback[0], traceback[1], traceback[2])

    @staticmethod
    def inner_reset_until_unique(boolean):
        traceback = [inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][4]]
        if boolean: Settings.__boolean_assert("special/inner_unique", boolean, traceback[0], traceback[1], traceback[2])