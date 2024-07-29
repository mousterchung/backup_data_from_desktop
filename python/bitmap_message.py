'''Bitmap Message, by Al Sweigart al@inventwithpython.com
Displays a text message according to the provided bitmap image.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, artistic'''
import sys
#(!)Try changing this multiline string to any image you like:
#There are 68 periods along the top and bottom of this string:
#(You can also copy and paste this string from
#https://inventwithpython.com/bitmapworld.txt)
bitmap='''
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................'''
print('Bitmap Message, by Al Sweigart al@inventwithpython')
print('Enter the message to display with the bitmap.')
message=input('> ')
if not message:sys.exit()
for line in bitmap.splitlines():#Loop over each line in the bitmap
    for i, bit in enumerate(line):#Loop over each character in the line
        if bit==' ':print(' ',end='')#Print an empty space since there's a space in the bitmap:
        else:print(message[i%len(message)],end='')#Print a character from the message
    print()#Print a newline.