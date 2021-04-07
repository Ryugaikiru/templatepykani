from discord.ext import commands
import os
import traceback
import random
import discord

bot = commands.Bot(!knhelp)
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()


def randomcrab():
    # カニを日本語で抽選
    crab = ['ズワイガニ', 'ガザミ', 'トラフカラッパ', 'エンコウガニ', 'ヒシガニ', 'ケガニ', 'ベニイワガニ', 'モクズガニ', 'アサヒガニ', 'ロブスター', 'ダンジネスクラブ', 'クリスマスアカガニ', 'ノコギリガザミ', 'オオホモラ', 'ヤシガニ', 'タラバガニ', 'オオカイカムリ', 'タカアシガニ', 'メタルクラブ', 'タスマニアオオガニ', 'シャコ', 'シオマネキ', 'ハナサキガニ']
    # カニの配列を日本語で作成
    return random.choice(crab)


def randomcrabEN():
    # カニを英語で抽選/ select random crab in english
    crabEN = ['Snow Crab', 'Blue Crab', 'Calappa', 'Long Arm Crab', 'Elbow Crab', 'Horsehair Crab', 'Red Rock Crab', 'Mitten Crab', 'Red Frog Crab', 'Lobster', 'Dungeness Crab', 'Christmas Red Crab', 'Mud Crab', 'Carrer Crab', 'Coconut Crab', 'King Crab', 'Sponge Crab', 'Spider Crab', 'Metal Crab', 'Tasmanian Giant', 'Mantis Shrimp', 'Fiddler Crab', 'Hanasaki Crab']
    # カニの配列を英語で作成/ Create Crab list in english
    return random.choice(crabEN)


def randomweapon():
    # 武器を日本語で抽選
    weapon = {"ステゴロ": '片手', "ナイフ": '片手', "ソード": '片手', "カタナ": '片手', "ショーテル": '片手', "レイピア": '片手', "ハンドアックス": '片手', "ダガー": '片手', "カタール": '片手', "コチョウトウ": '片手', "ビームセイバー": '片手', "ヘビーソード": '片手', "ジャバラケン": '片手', "ジャベリン": '片手', "ランス": '片手', "トライデント": '片手', "バール": '片手', "バット": '片手', "メイス": '片手', "ウォーハンマー": '片手', "トンファー": '片手', "フレイル": '片手', "ヌンチャク": '片手', "ガーダ": '片手', "リボルバー": '片手', "ショットガン": '片手', "アックスガン": '片手', "サイ": '片手', "シールド": '片手', "クサリガマ": '片手', "ジェット": '片手', "アンカー": '片手', "テッセン": '片手', "ブーメラン": '片手', "ドリル": '片手', "パイルバンカー": '片手', "クレイモア": '両手', "グアンダオ": '両手', "ハルバード": '両手', "チェーンソー": '両手', "グレートハンマー": '両手', "ノダチ": '両手', "ダブルセイバー": '両手', "エクスカニバー": '両手', "バルディッシュ": '両手', "サンセツコン": '両手', "アザラシ": 'のりもの', "スクーター": 'のりもの'}
    # 武器の辞書を日本語で作成
    names = list(weapon)  # 武器の名前リストを作成
    r = random.choice(names)  # 武器を名前から抽選
    rtype = weapon[r]  # 武器の種類を取得
    weaponl = []  # 左に装備可能な武器を入れる空の配列を作成
    if rtype == '片手':
        # 片手武器を装備していた場合
        for num in range(48):
            # 両手以外、つまり片手武器とのりものをリストに追加
            if weapon[names[num]] != '両手':
                weaponl.append(names[num])
    elif rtype == 'のりもの':
        # のりものを装備していた場合
        for num in range(48):
            # 片手武器のみをリストに追加
            if weapon[names[num]] == '片手':
                weaponl.append(names[num])
    else:
        # 両手武器を装備していた場合
        weaponl.append(r)
    larm = random.choice(weaponl)
    # 左に同じ武器名をコピー
    return [r, larm]


def randomweaponEN():
    # 武器を英語で抽選/ select random weapon in english
    weapon = {"Claw": '片手', "Knife": '片手', "Sword": '片手', "Katana": '片手', "Shotel": '片手', "Rapier": '片手', "Hand Axe": '片手', "Dagger": '片手', "Katar": '片手', "Butterfly Sword": '片手', "Beam Saber": '片手', "Heavy Sword": '片手', "Whip Sword": '片手', "Javelin": '片手', "Lance": '片手', "Trident": '片手', "Crowbar": '片手', "Bat": '片手', "Mace": '片手', "War Hammer": '片手', "Tonfa": '片手', "Flair": '片手', "Nunchaku": '片手', "Gada": '片手', "Revolver": '片手', "Shotgun": '片手', "Axe gun": '片手', "Sai": '片手', "Shield": '片手', "Sickle": '片手', "Jet": '片手', "Anchor": '片手', "Iron Fan": '片手', "Boomerang": '片手', "Dril": '片手', "Pile Banker": '片手', "Claymore": '両手', "Guandao": '両手', "Halberd": '両手', "Chainsaw": '両手', "Great Hammer": '両手', "Nodachi": '両手', "Double Saber": '両手', "Excalibur": '両手', "Bardiche": '両手', "3 Section Staff": '両手', "Seal": 'のりもの', "Scooter": 'のりもの'}
    # 武器の辞書を英語で作成/ Create the dict of weapons
    names = list(weapon)  # 武器の名前リストを作成/ Create the list of weapons names
    r = random.choice(names)  # 武器を名前から抽選/ Select random weapon from name
    rtype = weapon[r]  # 武器の種類を取得/ Get the weapon tipe
    weaponl = []  # 左に装備可能な武器を入れる空の配列を作成/ Create the empty list of weapons that is possible to equip on the left arm
    if rtype == '片手':
        # 片手武器を装備していた場合/ if the equipment is a one handed weapon
        for num in range(48):
            # 両手以外、つまり片手武器とのりものをリストに追加/ add one handed weapon and　vehicle to the possible weapon list
            if weapon[names[num]] != '両手':
                weaponl.append(names[num])
    elif rtype == 'のりもの':
        # のりものを装備していた場合/ if the equipment is a vehicle
        for num in range(48):
            # 片手武器のみをリストに追加
            if weapon[names[num]] == '片手':
                weaponl.append(names[num])
    else:
        # 両手武器を装備していた場合/ if the equipment is an two handed weapon
        # 左に同じ武器名をコピー/ copy the name of weapon to  the left
        weaponl.append(r)
    larm = random.choice(weaponl)
    return [r, larm]


def shuffling():
    # 左右の武器が偏らないようにランダムで入れ替える
    if random.randint(0, 1) == 0:  # 0がでたら
        sayuu = randomweapon()
        return ('右手：' + sayuu[0] + '　左手：' + sayuu[1])  # 入れ替えない
    else: # 1がでたら
        sayuu = randomweapon()
        return ('右手：' + sayuu[1] + '　左手：' + sayuu[0])  # 入れ替える


def shufflingEN():
    # 左右の武器が偏らないようにランダムで入れ替える/ Randomly replace the left and right weapons so that they are not biased
    if random.randint(0, 1) == 0:  # 0がでたら/ If 0 appears
        sayuu = randomweaponEN()
        return ('Right:' + sayuu[0] + '　Left:' + sayuu[1])  # 入れ替えない/ Change
    else: # 1がでたら/ If 1 appears
        sayuu = randomweaponEN()
        return ('Right:' + sayuu[1] + '　Left:' + sayuu[0])  # 入れ替える/ Don't change


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="稼働中", type=1))


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def pingping(ctx):
    """特に意味はない"""
    await ctx.send('pong')


@bot.command()
async def ran(ctx):
    """カニと武器を一人分抽選する。お一人様用。"""
    weaponset = shuffling()
    arandomizer = '\nあなたは - ' + randomcrab() + '\n' + weaponset
    await ctx.send(arandomizer)


@bot.command()
async def sin(ctx):
    """カニと武器を二人分抽選する。タイマン時に便利。"""
    weaponset = shuffling()
    brandomizer = '\nホスト：' + randomcrab() + '\n' + weaponset
    weaponset = shuffling()
    brandomizer += '\n' + '\n' + 'ゲスト：' + randomcrab() + '\n' + weaponset
    await ctx.send(brandomizer)


@bot.command()
async def tag(ctx):
    """カニと武器を四人分抽選する。タッグバトル時に使える（sinを二回使っても問題はない）。"""
    weaponset = shuffling()
    drandomizer = '\nホスト：' + randomcrab() + '\n' + weaponset
    weaponset = shuffling()
    drandomizer += '\n' + '\n' + 'ホストの相棒：' + randomcrab() + '\n' + weaponset
    weaponset = shuffling()
    drandomizer += '\n' + '\n' + '左のゲスト：' + randomcrab() + '\n' + weaponset
    weaponset = shuffling()
    drandomizer += '\n' + '\n' + '右のゲスト：' + randomcrab() + '\n' + weaponset
    await ctx.send(drandomizer)


@bot.command()
async def ranEN(ctx):
    """Randomize one set of crabs and weapons. For one person."""
    weaponset = shufflingEN()
    arandomizer = '\nYou are - ' + randomcrabEN() + '\n' + weaponset
    await ctx.send(arandomizer)


@bot.command()
async def sinEN(ctx):
    """Randomize two set of crabs and weapons. For one-on-one battle"""
    weaponset = shufflingEN()
    brandomizer = '\nHost:' + randomcrabEN() + '\n' + weaponset
    weaponset = shufflingEN)
    brandomizer += '\n' + '\n' + 'guest：' + randomcrabEN() + '\n' + weaponset
    await ctx.send(brandomizer)


@bot.command()
async def tagEN(ctx):
    """Randomize four set of crabs and weapons. For tag buttle (no problem if you wnat to use sinEN command twice)."""
    weaponset = shuffling()
    drandomizer = '\nHost:' + randomcrabEN() + '\n' + weaponset
    weaponset = shuffling()
    drandomizer += '\n' + '\n' + "Host's buddy:" + randomcrabEN() + '\n' + weaponset
    weaponset = shuffling()
    drandomizer += '\n' + '\n' + 'Left guest:' + randomcrabEN() + '\n' + weaponset
    weaponset = shuffling()
    drandomizer += '\n' + '\n' + 'Right guest:' + randomcrabEN() + '\n' + weaponset
    await ctx.send(drandomizer)


bot.run(token)
