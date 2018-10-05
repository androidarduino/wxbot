# -*- coding: utf-8 -*-

from wxpy import *
import time

bot=Bot('bot.pkl', console_qr=True)

''' Validation Request '''

def valid_msg(msg):
	groups = bot.groups()
	jia = u'加' in msg.text.lower()
	qun = u'群' in msg.text.lower()
	qunming = False
	for grpname in groups:
		qunming = (grpname.name in msg.text.lower())
		if (qunming):
			break
	if (jia and qun and (not qunming)):
		msg.reply(u'欢迎使用拉群助手。给我发 [都有什么群] 可以查看群列表， 给我发 [加群 XXX] 可以自动拉群，XXX是群的全名，记得是全名哦，少一个字和符号不行。')
	if (jia and qun and qunming):
		return grpname
	else:
		return False

''' Method to add people to a group '''

def invite(user, grp):
	time.sleep(2)
	if (len(grp)==500):
		user.send(u'此群已满，请加新群')
		return
	grp.add_members(user, use_invitation=True)

''' Event listener '''

@bot.register(msg_types=FRIENDS, except_self=False)
def new_friends(msg):
	user = msg.card.accept()
	pull_friend(msg)

@bot.register(Group, TEXT, except_self=False)
def group_pull(msg):
	if (isinstance(msg.chat, Group) and not msg.is_at):
		return
	pull_friend(msg)

@bot.register(Friend, TEXT, except_self=False)
def pull_friend(msg):
	global global_msg
	print msg
	global_msg = msg
	user = msg.sender
	if (u"都有什么群" in msg.text.lower()):
		user.send(list_groups())
	if valid_msg(msg):
		invite(user, valid_msg(msg))

def list_groups():
	time.sleep(1)
	groups = bot.groups()
	msg = "List of groups: \n"
	for group in groups:
		if u"亚麻" in group.name:
			msg = msg + group.name + " " + str(len(group)) + "\n"
	return msg

embed()
