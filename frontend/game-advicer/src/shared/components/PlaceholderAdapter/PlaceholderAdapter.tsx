import React from 'react'
import { Placeholder } from '@vkontakte/vkui'
import { PlaceholderProps } from '@vkontakte/vkui/dist/components/Placeholder/Placeholder'

/** Адаптер для компонента placeholder */
export const PlaceholderAdapter: React.FC<PlaceholderProps> = React.memo(
    (props) =>
        (
            <>
                <Placeholder {...props} />
            </>
        )
)
