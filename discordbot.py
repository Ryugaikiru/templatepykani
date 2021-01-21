import discord
from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='!kn')
token = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def pinpin(ctx):
    await ctx.send('pong')


@bot.command()
async def ran(ctx):
    weaponset = shuffling()
    arandomizer = '\nあなたは - ' + randomcrab() + '\n' + weaponset
    await ctx.send(arandomizer)


@bot.command()
async def sin(ctx):
    weaponset = shuffling()
    brandomizer = '\nホスト：' + randomcrab() + '\n' + weaponset
    weaponset = shuffling()
    brandomizer += '\n' + '\n' + 'ゲスト：' + randomcrab() + '\n' + weaponset
    await ctx.send(brandomizer)


@bot.command()
async def tag(ctx):
    weaponset = shuffling()
    drandomizer = '\nホスト：' + randomcrab() + '\n' + weaponset
    weaponset = shuffling()
    drandomizer += '\n' + '\n' + 'ホストのパートナー：' + randomcrab() + '\n' + weaponset
    weaponset = shuffling()
    drandomizer += '\n' + '\n' + 'ホストの対面：' + randomcrab() + '\n' + weaponset
    weaponset = shuffling()
    drandomizer += '\n' + '\n' + '対面のパートナー：' + randomcrab() + '\n' + weaponset
    await ctx.send(drandomizer)


bot.run(token)

def randomcrab():
    crab = ['ズワイガニ', 'ガザミ', 'トラフカラッパ', 'エンコウガニ', 'ヒシガニ', 'ケガニ', 'ベニイワガニ', 'モズクガニ', 'アサヒガニ', 'ロブスター', 'ダンジネスクラブ', 'クリスマスアカガニ', 'ノコギリガザミ', 'オオホモラ', 'ヤシガニ', 'タラバガニ', 'オオカイカムリ', 'タカアシガニ', 'メタルクラブ', 'タスマニアオオガニ', 'シャコ', 'シオマネキ', 'ハナサキガニ']
    return random.choice(crab)

def randomweapon():
    weapon = {"ステゴロ": '片手', "ナイフ": '片手', "ソード": '片手', "カタナ": '片手', "ショーテル": '片手', "レイピア": '片手', "ハンドアックス": '片手', "ダガー": '片手', "カタール": '片手', "コチョウトウ": '片手', "ビームセイバー": '片手', "ヘビーソード": '片手', "ジャバラケン": '片手', "ジャベリン": '片手', "ランス": '片手', "トライデント": '片手', "バール": '片手', "バット": '片手', "メイス": '片手', "ウォーハンマー": '片手', "トンファー": '片手', "フレイル": '片手', "ヌンチャク": '片手', "ガーダ": '片手', "リボルバー": '片手', "ショットガン": '片手', "アックスガン": '片手', "サイ": '片手', "シールド": '片手', "クサリガマ": '片手', "ジェット": '片手', "アンカー": '片手', "テッセン": '片手', "ブーメラン": '片手', "ドリル": '片手', "パイルバンカー": '片手', "クレイモア": '両手', "グアンダオ": '両手', "ハルバード": '両手', "チェーンソー": '両手', "グレートハンマー": '両手', "ノダチ": '両手', "ダブルセイバー": '両手', "エクスカニバー": '両手', "バルディッシュ": '両手', "サンセツコン": '両手', "アザラシ": 'のりもの', "スクーター": 'のりもの'}
    names = list(weapon)
    r = random.choice(names)
    rtype = weapon[r]
    weaponl = []
    if rtype == '片手':
        for num in range(48):
            if weapon[names[num]] == '片手':
                weaponl.append(names[num])
    elif rtype == 'のりもの':
        for num in range(48):
            if weapon[names[num]] == 'のりもの':
                weaponl.append(names[num])
    else:
        weaponl.append(r)
    larm = random.choice(weaponl)
    return [r, larm]


def shuffling():
    if random.int(0, 1) == 0:
        sayuu = randomweapon()
        return ('右手：' + sayuu[0] + '　左手：' + sayuu[1])
    else:
        sayuu = randomweapon()
        return = ('右手：' + sayuu[1] + '　左手：' + sayuu[0])
