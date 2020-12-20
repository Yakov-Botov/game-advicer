import React, { useMemo } from 'react'
import {
    Icon28LikeOutline,
    Icon28GameOutline,
    Icon28UserCircleOutline,
} from '@vkontakte/icons'
import { IconsAdapterProps } from '.'

export const IconsAdapter: React.FC<IconsAdapterProps> = React.memo(
    ({ iconType, ...otherProps }) => {
        const iconRender = useMemo(() => {
            switch (iconType) {
                case 'Icon28GameOutline':
                    return <Icon28GameOutline {...otherProps} />
                case 'Icon28LikeOutline':
                    return <Icon28LikeOutline {...otherProps} />
                case 'Icon28UserCircleOutline':
                    return <Icon28UserCircleOutline {...otherProps} />
            }
        }, [iconType, otherProps])

        return <>{ iconRender }</>
    }
)
