one = pic_1
two = pic_2
kps1,descs1=extract_features(one)
kps2,descs2=extract_features(two)
matches=match_kp(descs1,descs2)
H=calc_H2(matches,kps1,kps2)
print("H:"+str(H))
top_right=np.array([two.shape[1],0],dtype="float32")
bot_right=np.array([two.shape[1],two.shape[0]],dtype="float32")
top_left=np.array([0,0],dtype="float32")
bot_left=np.array([0,two.shape[0]],dtype="float32")
#For some reason, perspective transform requires crazy high dimensionality
proj_corns=cv2.perspectiveTransform(np.array([[top_right,bot_right,top_left,bot_left]]),H)
green=np.transpose(np.ndarray.reshape(proj_corns,(4,2)))
print(green)
# plt.plot(green[0],green[1],"or")
min_x=np.min(green[0])
max_x=np.max(green[0])
size_x=abs(max_x-min_x)
min_y=np.min(green[1])
max_y=np.max(green[1])
size_y=abs(max_y-min_y)
print(size_x,size_y)
ones=np.array([1,1,1])
x_shift=-min_x
print("xshift:"+str(x_shift))
#     x_shift=abs(np.dot(H,ones)[0])
# trans=np.array([[1,0,x_shift],[0,1,0],[0,0,1]])
result = cv2.warpPerspective(two, H,(max_x, max_y))
# result = cv2.warpPerspective(one, np.dot(H,trans),(size_x, size_y))

#     result = cv2.warpPerspective(one, H,(one.shape[1] + two.shape[1], one.shape[0]))

warp1=result.copy()
result[0:one.shape[0], 0:one.shape[1]] = one
plt.imshow( result)

new_corns=cv2.perspectiveTransform(np.array([[top_right,bot_right,top_left,bot_left]]),np.dot(H,trans))
red=np.transpose(np.ndarray.reshape(new_corns,(4,2)))
print(red)
plt.plot(red[0],red[1],"or")
plt.plot(green[0],green[1],"og")