'''
Two sun

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
'''
# range(start,stop,interval)


# def twoSum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# nums = [2, 7, 11, 15]
# target = 18

# print(twoSum(nums,target))


"""
Palindrome Number
    
Input: x = 121
Output: true

Input: x = -121
Output: false

index position = [0,5,10,15,20,25,30,35,40]
                  0,1, 2, 3, 4, 5, 6, 7, 8
                 -9,-8,-7,-6,-5,-4,-3,-2,-1
                 
Indexing = [start:stop:step]

Palindrome = [::-1] 

"""

# def Palindrome_test(x):
#     if x < 0 or x == int(str(x)[::-1]):
#         return False
#     # return False if x < 0 else x == int(str(x)[::-1])
# print(Palindrome_test(110))


    """
    exception practice
    """
    
    def exception():
        ok_msg="ok"
        err_msg="failed"
        try:
            extra = {'addr': request.META['REMOTE_ADDR']}
            order_ID = request.POST.get('order_id', '')
            order_code = request.POST.get('order_code', '')

            try:
                resp = OrderCode.objects.get(order=order_ID, code=order_code, active=True)
            except OrderCode.DoesNotExist:
                raise ValueError('The order code does not exists')

            results = {
                'Order_ID': resp.order_id,
                'Order_Code': resp.code,
                'Approval': resp.approval,
                'Auto_Engine': resp.auto_engine,
                'Mile_Stone': resp.mile_stone
            }
        except ValueError as e:
            log.error(get_log_msg(ERR_MSG, add=f'{str(e)}'), extra=extra)
            return HttpResponse(ERR_MSG, content_type='text/plain', status=400)
        except Exception as e:
            log.error(get_log_msg(ERR_MSG, add=f'{str(e)}'), extra=extra, exc_info=True)
            return HttpResponse(ERR_MSG, content_type='text/plain', status=501)
        else:
            log.info(get_log_msg(OK_MSG, add=f'Code: {order_code}'), extra=extra)
            return JsonResponse({'msg': OK_MSG, 'data': results})