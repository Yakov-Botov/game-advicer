import React from 'react'
import { Col, ColProps } from 'react-flexbox-grid'

type ColAdapterProps = ColProps

/** DI обертка над компонентом row для grid приложения  */
export const ColAdapter: React.FC<ColAdapterProps> = React.memo((props) => {
    return <Col {...props} />
})