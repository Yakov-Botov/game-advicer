import {Icon28LikeOutlineProps} from "@vkontakte/icons/dist/28/like_outline";

type IconTypes =
    | 'IconLikeOutline'
    | 'IconGameOutline'
    | 'IconUserCircleOutline'
    | 'IconMoreHorizontal'
    | 'IconStars3Outlined'

export interface IconsAdapterProps extends Icon28LikeOutlineProps {
    iconType: IconTypes
}