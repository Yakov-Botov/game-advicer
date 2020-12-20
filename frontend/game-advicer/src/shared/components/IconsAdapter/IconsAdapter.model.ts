import {Icon28LikeOutlineProps} from "@vkontakte/icons/dist/28/like_outline";

type IconTypes =
    | 'Icon28LikeOutline'
    | 'Icon28GameOutline'
    | 'Icon28UserCircleOutline'

export interface IconsAdapterProps extends Icon28LikeOutlineProps {
    iconType: IconTypes
}