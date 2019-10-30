from argparse import ArgumentParser

from . import robots_loader

ROBOTS = [
    'anymal', 'hyq', 'solo', 'solo12', 'talos', 'talos_arm', 'talos_legs', 'tiago', 'tiago_no_hand', 'icub', 'ur5', 'hector', 'double_pendulum'
]

parser = ArgumentParser()
parser.add_argument('robot', nargs='?', default=ROBOTS[0], choices=ROBOTS)

args = parser.parse_args()

if args.robot == 'anymal':
    anymal = robots_loader.loadANYmal()
    anymal.initViewer(loadModel=True)
    anymal.display(anymal.q0)

if args.robot == 'hyq':
    hyq = robots_loader.loadHyQ()
    hyq.initViewer(loadModel=True)
    hyq.display(hyq.q0)

if args.robot == 'solo':
    solo = robots_loader.loadSolo()
    solo.initViewer(loadModel=True)
    solo.display(solo.q0)

if args.robot == 'solo12':
    solo = robots_loader.loadSolo(False)
    solo.initViewer(loadModel=True)
    solo.display(solo.q0)

elif args.robot == 'talos':
    talos = robots_loader.loadTalos()
    talos.initViewer(loadModel=True)
    talos.display(talos.q0)

elif args.robot == 'talos_arm':
    talos_arm = robots_loader.loadTalosArm()
    talos_arm.initViewer(loadModel=True)
    talos_arm.display(talos_arm.q0)

if args.robot == 'talos_legs':
    talos_legs = robots_loader.loadTalosLegs()
    talos_legs.initViewer(loadModel=True)
    talos_legs.display(talos_legs.q0)

elif args.robot == 'tiago':
    tiago = robots_loader.loadTiago()
    tiago.initViewer(loadModel=True)
    tiago.display(tiago.q0)

elif args.robot == 'tiago_no_hand':
    tiago_no_hand = robots_loader.loadTiagoNoHand()
    tiago_no_hand.initViewer(loadModel=True)
    tiago_no_hand.display(tiago_no_hand.q0)

elif args.robot == 'icub':
    icub = robots_loader.loadICub()
    icub.initViewer(loadModel=True)
    icub.display(icub.q0)

elif args.robot == 'ur5':
    ur5 = robots_loader.loadUR()
    ur5.initViewer(loadModel=True)
    ur5.display(ur5.q0)

if args.robot == 'hector':
    hector = robots_loader.loadHector()
    hector.initViewer(loadModel=True)
    hector.display(hector.q0)


if args.robot == 'double_pendulum':
    planar2dof = robots_loader.load2dof()
    planar2dof.initViewer(loadModel=True)
    planar2dof.display(planar2dof.q0)
