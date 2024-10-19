"""

** coded by Sathwik,Sourav,Sinchan,pratyush  on 19/10/2024 **
** God Speed **
** May all beings be Happy,Peaceful,Liberated **

"""
import os
from config import config
traindir = os.path.join(config.parent,'experiments','training')

tb = 'tensorboard --logdir={} --port 6006'.format(traindir)

os.system(tb)

exit(0)
