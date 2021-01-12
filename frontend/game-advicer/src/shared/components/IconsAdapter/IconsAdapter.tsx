import React, { useMemo } from 'react'
import {
    Icon28LikeOutline,
    Icon28GameOutline,
    Icon28UserCircleOutline,
    Icon28MoreHorizontal,
    Icon56Stars3Outline,
} from '@vkontakte/icons'
import { IconsAdapterProps } from '.'

/** Компонент-адаптер для использования иконок в приложении */
export const IconsAdapter: React.FC<IconsAdapterProps> = React.memo(
    ({ iconType, ...otherProps }) => {
        /** TODO: нужно реализовать систему размеров (sm, md, xl) и уйти от жесткой привязки размеров иконок в VKUI */
        const iconRender = useMemo(() => {
            switch (iconType) {
                case 'IconGameOutline':
                    return <Icon28GameOutline {...otherProps} />
                case 'IconLikeOutline':
                    return <Icon28LikeOutline {...otherProps} />
                case 'IconUserCircleOutline':
                    return <Icon28UserCircleOutline {...otherProps} />
                case 'IconMoreHorizontal':
                    return <Icon28MoreHorizontal {...otherProps} />
                case 'IconStars3Outlined':
                    return <Icon56Stars3Outline {...otherProps} />
            }
        }, [iconType, otherProps])

        return <>{iconRender}</>
    }
)
