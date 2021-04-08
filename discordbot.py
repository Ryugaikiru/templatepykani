from discord.ext import commands
import os
import traceback
import random
import discord

bot = commands.Bot(command_prefix='!kn')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()


def randomcrab():
    # カニを日本語で抽選
    crab = ['ズワイガニ', 'ガザミ', 'トラフカラッパ', 'エンコウガニ', 'ヒシガニ', 'ケガニ', 'ベニイワガニ', 'モクズガニ', 'アサヒガニ', 'ロブスター', 'ダンジネスクラブ', 'クリスマスアカガニ', 'ノコギリガザミ', 'オオホモラ', 'ヤシガニ', 'タラバガニ', 'オオカイカムリ', 'タカアシガニ', 'メタルクラブ', 'タスマニアオオガニ', 'シャコ', 'シオマネキ', 'ハナサキガニ']
    # カニの配列を日本語で作成
    return random.choice(crab)


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


def shuffling():
    # 左右の武器が偏らないようにランダムで入れ替える
    if random.randint(0, 1) == 0:  # 0がでたら
        sayuu = randomweapon()
        return ('右手：' + sayuu[0] + '　左手：' + sayuu[1])  # 入れ替えない
    else:  # 1がでたら
        sayuu = randomweapon()
        return ('右手：' + sayuu[1] + '　左手：' + sayuu[0])  # 入れ替える


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="!knhelp", type=1))


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


bot.run(token)
